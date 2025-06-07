import logging
import aiohttp
import socket
import ipaddress
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

class MCPServerConnectionError(Exception):
    pass

class EdgarClientException(Exception):
    pass

def is_url_allowed(url: str) -> bool:
    """
    Returns True if the URL is safe to be navigated to from the server (prevents SSRF), else False.
    Only allows http/https public network addresses.
    """
    try:
        parsed = urlparse(url)
        # Only http and https are permitted
        if parsed.scheme not in ('http', 'https'):
            logger.warning(f"Blocked navigation to URL with unsupported scheme: {url}")
            return False

        hostname = parsed.hostname
        if not hostname:
            logger.warning(f"Blocked navigation to URL with missing hostname: {url}")
            return False

        # Attempt to resolve the hostname to one or more IP addresses
        try:
            addresses = set()
            for result in socket.getaddrinfo(hostname, None):
                ip = result[4][0]
                addresses.add(ip)
        except Exception as e:
            logger.warning(f"Blocked navigation to URL due to DNS resolution failure: {url}, error: {e}")
            return False

        # Check all addresses to ensure none are in a private, loopback, or link-local range
        for ip in addresses:
            try:
                ip_obj = ipaddress.ip_address(ip)
                # Blocks loopback, private, link-local, reserved & multicast
                if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_reserved or ip_obj.is_multicast:
                    logger.warning(f"Blocked navigation to private/loopback/link-local/reserved/multicast IP ({ip}) for URL: {url}")
                    return False
            except ValueError:
                # Not a valid IP (should not happen due to how getaddrinfo works)
                logger.warning(f"Blocked navigation to URL with invalid resolved IP: {url}")
                return False

        # All checks passed, URL is safe
        return True
    except Exception as e:
        logger.warning(f"Blocked navigation to URL due to validation error: {url}, error: {e}")
        return False

class EdgarClient:
    # ... other methods and __init__ ...

    async def navigate(self, url: str) -> bool:
        """Navigate the browser to a URL.
        
        Args:
            url: URL to navigate to
            
        Returns:
            bool: True if navigation was successful, False otherwise
                
        Raises:
            MCPServerConnectionError: If navigation fails
            RuntimeError: If no active session
        """
        if not self.session_id:
            self.session_id = await self._create_session()

        # SSRF prevention: validate and allow-list navigation URLs
        if not is_url_allowed(url):
            logger.error(f"Navigation blocked: URL failed validation or points to internal/reserved resource: {url}")
            return False
            
        try:
            logger.info(f"Navigating to {url}")
            
            # Use the execute endpoint with navigate command instead of direct navigate endpoint
            async with self.session.post(
                f"{self.mcp_server_url}/session/{self.session_id}/execute",
                headers=self.headers,
                json={
                    "command": "navigate",
                    "args": {"url": url}
                }
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"Navigation failed: {response.status}, {error_text}")
                    return False
                
                logger.info(f"Successfully navigated to {url}")
                return True
                
        except aiohttp.ClientError as e:
            logger.error(f"Navigation failed due to connection error: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during navigation: {e}")
            return False
        
    async def get_page_content(self) -> str:
        """Get the current page content using the execute command.
        
        Returns:
            HTML content of the current page
            
        Raises:
            EdgarClientException: If content retrieval fails
        """
        if not self.session_id:
            self.session_id = await self._create_session()
            
        try:
            logger.info("Retrieving page content via execute command")
            async with self.session.post(
                f"{self.mcp_server_url}/session/{self.session_id}/execute",
                headers=self.headers,
                json={"command": "content"}
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"Content retrieval failed: {response.status}, {error_text}")
                    raise EdgarClientException(f"Content retrieval failed: {error_text}")
                data = await response.json()
                content = data.get("content", "")
                logger.info(f"Retrieved {len(content)} bytes of content")
                return content
        except aiohttp.ClientError as e:
            logger.error(f"Content retrieval failed due to connection error: {e}")
            raise EdgarClientException(f"Content retrieval failed: {e}")