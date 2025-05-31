# SEC EDGAR Financial Insight Agent

> Hackathon project for Hacking Agents Hackathon NYC (May 30-31, 2025)

## Project Overview

This project combines SEC EDGAR financial data extraction with Langflow agent capabilities to create an AI assistant that helps investors understand complex financial information through natural language interaction.

## Hackathon Requirements

- **Main Technology**: Langflow
- **Partner Technologies**: DigitalOcean for hosting and database, DataStax Astra DB (optional vector DB)
- **Theme**: Building AI agents that provide real value

## Technical Architecture

┌─────────────────┐       ┌──────────────────┐      ┌──────────────────┐
│                 │       │                  │      │                  │
│  Langflow Agent ├───────┤  SEC EDGAR Tools ├──────┤  Vector Store    │
│  (Custom Flow)  │       │  (Python Class)  │      │  (MongoDB/Astra) │
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

**Architecture Notes:**
- Langflow Agent (custom flow) interfaces with both chat UI and SEC EDGAR tools.
- SEC EDGAR Tools connect to both the vector store (MongoDB or Astra DB) and the SEC EDGAR API.
- Data flows between components in a logical structure for agent-based financial analysis.

---

## Setup Instructions

### Prerequisites
- Python 3.10+ (Langflow requirement)
- DigitalOcean account with API access
- Langflow installed locally or deployed
- (Optional) DataStax Astra DB account for Cassandra-based vector storage

### Environment Setup
1. Clone this repo
2. Install dependencies:  
   ```sh
   pip install -r hackathon-langflow/requirements.txt
   ```
3. Set up cloud resources (DigitalOcean or Astra DB)

---

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
```

- **App Platform:** Deploy your Langflow app or API for easy demo and scaling.
- **Droplets:** For custom compute or GPU needs.
- **MCP Server:** For deploying and managing apps on App Platform.

---

### (Optional) Using DataStax Astra DB as Vector Store

1. **Sign up for Astra DB:**  
   https://astra.datastax.com/

2. **Create a database with vector search enabled.**

3. **Download your Secure Connect Bundle and note your client ID/secret.**

4. **Install required packages:**  
   ```sh
   pip install cassio langchain-astra
   ```

5. **Set environment variables:**  
   ```sh
   export ASTRA_DB_SECURE_BUNDLE_PATH=/path/to/secure-connect-database_name.zip
   export ASTRA_DB_CLIENT_ID=your_client_id
   export ASTRA_DB_CLIENT_SECRET=your_client_secret
   export ASTRA_DB_KEYSPACE=your_keyspace
   ```

6. **Sample integration code:**
   ```python
   from langchain_astra.vectorstores import AstraDB
   from langchain.embeddings.openai import OpenAIEmbeddings

   embeddings = OpenAIEmbeddings()
   vectorstore = AstraDB(
       embedding=embeddings,
       collection_name="sec_edgar_vectors",
       token="your_client_secret",
       api_endpoint="https://your-db-id-us-east1.apps.astra.datastax.com",
       namespace="your_keyspace"
   )
   ```

---

## Running Langflow

```sh
langflow run
```
or, if using `uv`:
```sh
uv run langflow run
```

The Langflow UI should now be accessible at [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## DigitalOcean Services You Can Leverage

- **Managed MongoDB**: Vector storage for embeddings and financial data.
- **App Platform**: Deploy your Langflow UI or backend API.
- **Droplets**: Custom compute or GPU for embeddings.
- **MCP Server**: Easy deployment and management of your app.

---

## Hackathon Tips

- Highlight your use of both Langflow and at least one partner tool (DigitalOcean, Astra DB, etc.) for prize eligibility.
- Mention your use of Astra DB for vector search if you want to impress DataStax judges.
- Use DigitalOcean’s App Platform or Managed MongoDB for the “Best Use Of DigitalOcean” prize.

---

## Resources

- [Langflow Docs](https://docs.langflow.org/)
- [Astra DB Vector Search](https://docs.datastax.com/en/astra/astra-db-vector-search.html)
- [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)
- [DigitalOcean MCP Server](https://github.com/digitalocean/digitalocean-mcp)