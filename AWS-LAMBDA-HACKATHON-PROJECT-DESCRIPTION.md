# AWS Lambda Hackathon Project: SEC Filing Extractor & Secure Serverless API

https://awslambdahackathon.devpost.com/

## Project Overview

### Project name
SEC Filing Extractor & Secure Serverless API

### Elevator pitch
Serverless AWS Lambda app that ingests, parses, and serves SEC EDGAR data via a secure API. Automated security scanning and AI-powered remediation ensure robust, production-ready code.

## Inspiration

The project was inspired by the need for scalable, secure, and real-time access to SEC EDGAR financial filings—critical for analysts, fintech apps, and compliance teams. Our team saw an opportunity to modernize and automate the extraction of financial statement data, moving beyond mock data and manual scraping to a robust, production-ready solution. The AWS Lambda Hackathon provided the perfect environment to showcase cloud-native best practices and security automation.

## What it does

SEC Filing Extractor & Secure Serverless API is a serverless application that ingests, parses, and serves SEC EDGAR filing data (such as balance sheets and income statements) via a secure API endpoint. Users can request structured financial data for any public company by ticker, form type, year, and quarter. Automated security scanning and AI-driven remediation are integrated throughout the development process to ensure robust protection of the production codebase.

## How we built it

- **Architecture:**  
  We used AWS Lambda (Python runtime) for serverless compute, API Gateway for secure endpoints, DynamoDB for optional data storage, and SST (Serverless Stack) for infrastructure as code.
- **Extraction Logic:**  
  All extraction logic is modularized in Python (`ingest_balance_sheet.py`, `ingest_income_statement.py`), leveraging open-source libraries (`sec-downloader`, `sec-parser`) for reliable parsing.
- **Lambda Handler:**  
  The Lambda handler (`src/lambda/handler.py`) acts as the bridge between API Gateway and our extraction modules, processing incoming requests and returning structured JSON responses.
- **Security:**  
  Automated security scanning and AI-powered remediation tools are integrated into the CI/CD workflow, ensuring vulnerabilities are detected and patched before deployment.
- **Testing:**  
  Full test coverage is provided, with tests based on real SEC 10-Q filings.

## Challenges we ran into

- **Parsing Real-World Filings:**  
  SEC filings are complex and inconsistent, requiring robust parsing logic and error handling.
- **Security Automation:**  
  Integrating automated scanning and remediation into a serverless workflow required careful orchestration and documentation.
- **Cloud-Native Integration:**  
  Connecting modular Python extraction logic with AWS Lambda and API Gateway, while maintaining clean interfaces and extensibility, was non-trivial.
- **Time Constraints:**  
  Delivering a production-ready, demo-able solution within the hackathon timeline was a significant challenge.

## Accomplishments that we're proud of

- Successfully moved from mock data to real SEC EDGAR data extraction.
- Built a modular, maintainable codebase that is ready for future enhancements (such as MCP server integration).
- Achieved full test coverage with real-world data.
- Integrated automated security scanning and remediation, demonstrating a security-first development approach.
- Delivered a working, serverless API that can be easily extended and scaled.

## What we learned

- The importance of modular design for maintainability and future integration.
- Best practices for building secure, serverless applications on AWS.
- How to automate security scanning and remediation in a modern CI/CD pipeline.
- The challenges and nuances of parsing real-world SEC filings at scale.

## What's next for SEC Filing Extractor & Secure Serverless API

- **MCP Server Integration:**  
  Extend the data ingestion layer to support browser automation and dynamic scraping via MCP server.
- **Advanced Analytics:**  
  Add endpoints for trend analysis, anomaly detection, and AI-powered insights.
- **Frontend Dashboard:**  
  Build a React/Next.js dashboard for interactive data exploration.
- **Open Data API:**  
  Expand API endpoints and documentation for broader community use.
- **Continuous Security:**  
  Further automate security scanning, triage, and remediation as the codebase grows.

---

## Built With

- Python (SEC data extraction)
- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- SST (Serverless Stack, TypeScript)
- React/Next.js (frontend)
- Pensar AI (security scanning)
- sec-downloader, sec-parser (Python libraries)

---

## Try it out

- [Demo site](https://your-demo-url.com)
- [GitHub repository](https://github.com/yourusername/your-repo)

---

## Project Media

- _Add screenshots or diagrams here_
- _Link to your video demo (YouTube, Vimeo, etc.)_

---

## Additional Info (for judges/organizers)

### Submitter Country of Residence
_Your country_

### AWS Tools Used
- AWS Lambda
- AWS API Gateway
- AWS Identity and Access Management (IAM)
- AWS CloudWatch (for logging/monitoring)
- AWS EKS

### How AWS Lambda was used

AWS Lambda serves as the core compute layer for the project. Each API request triggers a Lambda function, which ingests, parses, and returns SEC EDGAR filing data on demand. Lambda functions are also integrated with security scanning and remediation workflows, ensuring that only secure, production-ready code is deployed.

### Advanced Lambda Use Cases (Inspired by [Pensar AI](https://docs.pensar.dev/quickstart))

- **Event-driven security scanning:** Lambda functions are triggered by S3 uploads or API events to scan code artifacts for vulnerabilities, mimicking Pensar AI’s automated security workflows.
- **Automated remediation:** Lambda can suggest or apply code fixes based on scan results, demonstrating AI-powered remediation.
- **Full-stack integration:** A React/Next.js frontend (provisioned via SST) interacts with Lambda APIs, showcasing end-to-end serverless workflows.
- **Lambda + EKS orchestration:** Demonstrates hybrid cloud-native patterns by having Lambda trigger jobs in EKS for scalable, containerized processing.

### Lambda Triggers Implemented

- API Gateway: Yes (primary trigger for all data extraction endpoints)
- EventBridge: No (unless you add scheduled or event-driven tasks)
- Others: None at this stage

### Submitter Type
_Individual/Team/Organization_

### Organization Name (if applicable)
_Your org (if any)_

### Public Code Repository
[GitHub repo URL]

---

## Security & Compliance

- Pensar AI scanning integrated at each milestone
- Remediation documented in PRs and code comments
- Security-focused architecture and workflows

---
