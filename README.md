# AI Automation Portfolio

> Production-ready AI automation systems built with n8n, Python, Claude, and Docker.
> Designed as a senior-level Upwork portfolio showcasing real-world business automation workflows.

---

## Overview

This repository contains three end-to-end automation projects that demonstrate how AI can eliminate manual, repetitive work in lead generation, customer support, and document processing. Each project ships with clean architecture, full test coverage, structured logging, and a Railway deployment guide.

**Stack:** n8n (self-hosted) · Python 3.11 · Claude AI · Docker · PostgreSQL · Railway

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Orchestration | n8n (self-hosted, Docker) | Workflow automation engine |
| Language | Python 3.11 | Business logic + AI services |
| AI | Claude (Anthropic) | Scoring, extraction, generation |
| Containers | Docker + docker-compose | Unified local + cloud runtime |
| Database | PostgreSQL 15 | Persistence for all services |
| Vector DB | ChromaDB | RAG embeddings (Project 2) |
| PDF generation | WeasyPrint | Invoice + report output (Project 3) |
| Testing | pytest | Unit + integration tests |
| Logging | loguru | Structured logs across all services |
| Deploy (primary) | Railway | Docker-native, ~$5/mo |
| Deploy (fallback) | Render (free tier) | Python-only services |

---

## Repository Structure

```
upwork-ai-automation-portfolio/
│
├── .claude/                          # Claude Code session context
│   ├── CLAUDE.md                     # Master context (auto-read)
│   ├── PROJECTS.md                   # Full specs for all 3 projects
│   ├── STANDARDS.md                  # Code standards + patterns
│   └── SPRINT.md                     # Sprint calendar + live status
│
├── project-1-lead-generation/        # Lead scoring + outreach automation
│   ├── n8n/workflow.json
│   ├── src/
│   ├── tests/
│   ├── data/sample_leads.csv
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── project-2-support-chatbot-rag/    # RAG-powered support agent
│   ├── n8n/workflow.json
│   ├── src/
│   ├── tests/
│   ├── data/knowledge_base/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── project-3-document-processing/    # Invoice + document AI extraction
│   ├── n8n/workflow.json
│   ├── src/
│   ├── tests/
│   ├── data/sample_documents/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── project-4-content-pipeline/       # Reserved
├── project-5-client-onboarding/      # Reserved
│
├── docker-compose.yml                # Base stack: n8n + PostgreSQL
├── .env.example                      # Required environment variables
└── README.md                         # This file
```

---

## Projects

### Project 1 — Lead Generation + Outreach Automation

**Status:** 🔄 In progress · Target close: Jun 16, 2026

Captures raw leads from CSV or webhook, enriches missing fields, scores each lead 1–10 with Claude's reasoning, and generates a personalized outreach message per contact. Output: enriched CSV + outreach JSON + summary report.

```
[Lead Source: CSV / webhook]
        ↓
[Data Enrichment: fill missing fields via rules]
        ↓
[AI Scoring: Claude scores each lead 1–10 with reasoning]
        ↓
[Outreach Generator: Claude writes personalized message per lead]
        ↓
[Output: enriched CSV + outreach messages JSON + summary report]
```

**Key components:** n8n orchestration · Python enrichment service · Claude scoring + copywriting · PostgreSQL lead registry · 50 synthetic B2B leads

---

### Project 2 — RAG Support Chatbot

**Status:** ⬜ Pending · Target close: Jun 20, 2026

Knowledge base ingestion pipeline (chunk → embed → store) paired with a Claude agent that answers support tickets with retrieved context and source citations. Replaces manual first-line support for small businesses.

```
[Knowledge Base: Markdown / PDF docs]
        ↓
[Ingestion Pipeline: chunk → embed → store in ChromaDB]
        ↓
[Support Query: ticket or chat message arrives]
        ↓
[RAG Retrieval: top-k relevant chunks fetched]
        ↓
[Claude Agent: generates response with retrieved context]
        ↓
[Output: answer + source citations + confidence score]
```

**Key components:** ChromaDB (self-hosted, Docker) · Python ingestion + retrieval · Claude RAG agent · 20 synthetic docs for fictional product "AcmeCRM"

---

### Project 3 — Document Processing / Invoicing

**Status:** ⬜ Pending · Target close: Jun 24, 2026

Reads PDF invoices and email attachments, extracts structured data with Claude, classifies document type, registers in PostgreSQL, and generates output invoices or summary reports as PDF.

```
[Input: PDF invoice/receipt OR email with attachment]
        ↓
[Extraction: Claude reads and extracts structured data]
        ↓
[Classification: document type detection + routing logic]
        ↓
[Registration: save to PostgreSQL with status + metadata]
        ↓
[Output generator: invoice PDF or summary report]
        ↓
[Notification: email/webhook trigger — simulated]
```

**Key components:** n8n routing · Python PDF extractor · Claude data extraction · PostgreSQL document registry · WeasyPrint PDF output · 10 synthetic invoice PDFs

---

## Running Locally with Docker

### Prerequisites

- Docker Desktop (or Docker Engine + Compose plugin)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Hakiller777/upwork-ai-automation-portfolio.git
cd upwork-ai-automation-portfolio
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in the required values (see comments inside the file). No real API keys are needed — all AI calls use simulated responses for local development.

### 3. Start the base stack

```bash
docker compose up -d
```

This starts:
- **n8n** at `http://localhost:5678`
- **PostgreSQL** on port `5432`

### 4. Start a specific project

Navigate to the project folder and start its services:

```bash
# Example — Project 1
cd project-1-lead-generation
docker compose up -d
```

Each project folder contains its own `docker-compose.yml` that extends the base stack.

### 5. Import the n8n workflow

1. Open n8n at `http://localhost:5678`
2. Go to **Workflows → Import from file**
3. Select `n8n/workflow.json` from the project folder

### 6. Run the tests

```bash
cd project-1-lead-generation
pip install -r requirements.txt
pytest tests/ -v
```

---

## Deployment (Railway)

Each project includes a step-by-step `DEPLOYMENT.md` covering Railway setup. The summary:

1. Create a Railway project and link the GitHub repo
2. Add a PostgreSQL service from the Railway marketplace
3. Set the environment variables from `.env.example`
4. Railway detects the `Dockerfile` and builds automatically
5. Import the n8n workflow JSON after the first successful deploy

Primary platform: **Railway** (Docker-native, ~$5/mo, public URL with SSL)  
Fallback: **Render free tier** (Python-only services, ~1 min cold start)

---

## Quality Standards

Every project in this repository ships with:

- **Unit tests** — pytest, happy path + edge cases + error cases per module
- **Error handling** — try/except with graceful degradation, no silent failures
- **Structured logging** — loguru, INFO for flow events, ERROR for exceptions
- **Clean architecture** — separated ingestion / processing / output layers
- **Architecture diagram** — Mermaid diagram in each project's README
- **Synthetic data only** — all sample data is 100% fictional

---

## Sprint Timeline

| Day | Date | Focus |
|---|---|---|
| 1–2 | Jun 12 | Repo setup, Kanban, base Docker, this README |
| 3–6 | Jun 13–16 | **Project 1** — Lead Generation |
| 7–10 | Jun 17–20 | **Project 2** — RAG Chatbot |
| 11–14 | Jun 21–24 | **Project 3** — Document Processing |
| 15 | Jun 25 | Final polish + Upwork profile ready |

---

## License

MIT — free to use as reference or template. All business data in this repo is synthetic and fictional.
