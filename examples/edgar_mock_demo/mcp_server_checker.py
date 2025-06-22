"""MCP server connectivity testing."""
import aiohttp
import logging
import os
from typing import Dict, Any, Optional
from urllib.parse import urlparse

# Root logger
logger = logging.getLogger(__name__)

# Constants for MCP server configuration
MCP_SERVER_URL_ENV = "MCP_SERVER_URL"
DEFAULT_MCP_SERVER_URL = "http://localhost:3000"

def _validate_server_url(url: str) -> Optional[str]:
    """
    Validate the MCP server URL to prevent SSRF.
    Only allow localhost URLs, with http or https scheme.
    Returns validated URL (canonicalized, no trailing /), or None if invalid.
    """
    try:
        parsed = urlparse(url)
        # Allow only http(s), localhost or 127.0.0.1, and (optionally) default port 3000
        if parsed.scheme not in ("http", "https"):
            return None

        if parsed.hostname not in ("localhost", "127.0.0.1", "::1"):
            return None

        # Optional: You may enforce port check if needed (e.g., only 3000)
        # If you wish, uncomment below to enforce strict port match
        # if parsed.port not in (3000, None):  # Allow default port 80 if not specified
        #     return None

        # Remove trailing slash if present
        canonical_url = parsed.geturl().rstrip('/')

        return canonical_url
    except Exception:
        return None

async def check_mcp_server(server_url=None):
    """Check if MCP server is running and provide connection details."""
    # Get server URL from argument, environment, or default
    mcp_server_url = server_url or os.environ.get(MCP_SERVER_URL_ENV, DEFAULT_MCP_SERVER_URL)
    validated_url = _validate_server_url(mcp_server_url)
    if not validated_url:
        print("\n❌ Invalid MCP server URL. Only http(s)://localhost[:port] or http(s)://127.0.0.1[:port] is allowed for security reasons.")
        print_troubleshooting_info(mcp_server_url)
        return False

    print("\n===== MCP Server Status Check =====\n")
    
    # Try root endpoint
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{validated_url}/"
            print(f"🔍 Checking MCP server at {url}...")
            
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    print(f"✅ MCP Server is RUNNING at {validated_url}")
                    
                else:
                    print(f"❌ MCP server returned status {response.status}")
                    print_troubleshooting_info(validated_url)
                    return False
        except Exception as e:
            print(f"❌ Cannot connect to MCP server: {e}")
            print_troubleshooting_info(validated_url)
            return False

async def close_test_session(session, server_url, session_id):
    """Close a test browser session."""
    validated_url = _validate_server_url(server_url)
    if not validated_url:
        print("\n❌ Invalid MCP server URL. Only http(s)://localhost[:port] or http(s)://127.0.0.1[:port] is allowed for security reasons.")
        return
    try:
        print(f"🔍 Closing test session {session_id}...")
        
        async with session.delete(
            f"{validated_url}/session/{session_id}"
        ) as response:
            if response.status == 200:
                print("✅ Successfully closed test session")
            else:
                print(f"⚠️ Session close returned status {response.status}")
    except Exception as e:
        print(f"⚠️ Error closing test session: {e}")

def print_troubleshooting_info(server_url):
    """Print troubleshooting information for connection issues."""
    print("\n🔧 TROUBLESHOOTING:")
    print("1. Is the MCP server running? Start it with:")
    print("   cd ../mcp-server-browserbase && npm start")
    print("\n2. Check the server URL:")
    print(f"   Current URL: {server_url}")
    print("   You can set MCP_SERVER_URL environment variable or use --server-url")
    print("\n3. Check for firewall or port issues:")
    print("   Make sure port 3000 (or your custom port) is accessible")
    print("\n4. Look for errors in the MCP server logs")
    print("\n5. Verify MCP server API endpoints:")
    print("   The server should respond to POST /session for creating a browser session")