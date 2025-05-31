# SEC EDGAR Financial Insight Agent

> Hackathon project for Hacking Agents Hackathon NYC (May 30-31, 2025)

## Project Overview

This project combines SEC EDGAR financial data extraction with Langflow agent capabilities to create an AI assistant that helps investors understand complex financial information through natural language interaction.

## Hackathon Requirements

- **Main Technology**: Langflow
- **Partner Technologies**: DigitalOcean for hosting and database
- **Theme**: Building AI agents that provide real value

## Technical Architecture

┌─────────────────┐       ┌──────────────────┐      ┌──────────────────┐
│                 │       │                  │      │                  │
│  Langflow Agent ├───────┤  SEC EDGAR Tools ├──────┤  DO MongoDB     │
│  (Custom Flow)  │       │  (Python Class)  │      │  (Vector Store)  │
│                 │       │                  │      │                  │
└─────────────────┘       └──────────────────┘      └──────────────────┘
        │                          │
        │                          │
        ▼                          ▼
┌─────────────────┐       ┌──────────────────┐
│                 │       │                  │
│  Chat Interface │       │  SEC EDGAR API   │
│  (Langflow UI)  │       │  (Mock/Real)     │
│                 │       │                  │
└─────────────────┘       └──────────────────┘

This diagram shows the architecture of your SEC EDGAR Financial Insight Agent with:

Langflow Agent (custom flow) interfacing with both chat UI and SEC EDGAR tools
SEC EDGAR Tools connecting to both the MongoDB vector store and the SEC EDGAR API
Data flowing between components in a logical structure for agent-based financial analysis

## Setup Instructions

### Prerequisites
- Python 3.10+ (Langflow requirement)
- DigitalOcean account with API access
- Langflow installed locally or deployed

### Environment Setup
1. Clone this repo
2. Install dependencies: `pip install -r hackathon-langflow/requirements.txt`
3. Set up DigitalOcean resources using MCP Server

### DigitalOcean Setup
```bash
# Set your DO API Token 
export DIGITALOCEAN_API_TOKEN='your-token'

# Deploy MongoDB for vector storage
npx @digitalocean/mcp create database \
  --name "sec-edgar-vectors" \
  --engine "mongodb" \
  --size "db-s-1vcpu-1gb" \
  --region "nyc1"
