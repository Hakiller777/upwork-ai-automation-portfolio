# Project Specifications

> Full specs for the 3 active portfolio projects.
> Read this file when working inside any project folder.

---

## Project #1 — Lead Generation + Outreach

**Folder:** `project-1-lead-generation/`
**Sprint window:** Prep #1 (Jun 17–19) + Days 3–6 · Close target: Jun 23
**Hours allocated:** ~17h

### What it does
Captures leads → enriches data → scores with AI → generates personalized
outreach messages. One of the highest-ROI automations on the market.

### Workflow (end-to-end)
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

### Tech components
- n8n workflow: orchestration
- Python service: enrichment logic + AI scoring
- Claude: scoring + message generation
- PostgreSQL: lead storage + status tracking
- Synthetic dataset: 50 realistic B2B leads (fictional companies only)

### Folder structure to produce
```
project-1-lead-generation/
├── n8n/
│   └── workflow.json              # Exportable n8n workflow
├── src/
│   ├── __init__.py
│   ├── config.py                  # Settings from env vars
│   ├── models.py                  # Pydantic data models
│   ├── enrichment.py              # Data enrichment logic
│   ├── scoring.py                 # Claude-powered AI scoring
│   └── outreach.py                # Personalized message generator
├── tests/
│   ├── conftest.py
│   ├── test_enrichment.py
│   ├── test_scoring.py
│   └── test_outreach.py
├── data/
│   └── sample_leads.csv           # 50 synthetic B2B leads
├── docker-compose.yml             # Project-specific (extends base)
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md                      # Cowork generates this
```

---

## Project #2 — RAG Support Chatbot

**Folder:** `project-2-support-chatbot-rag/`
**Sprint window:** Days 7–10 · Close target: Jun 27
**Hours allocated:** ~17h

### What it does
Knowledge base (product docs + FAQs) + AI agent that answers support
tickets and chats with real context via RAG (Retrieval-Augmented Generation).
High ROI for small businesses replacing manual first-line support.

### Workflow (end-to-end)
```
[Knowledge Base: Markdown / PDF docs]
        ↓
[Ingestion Pipeline: chunk → embed → store in vector DB]
        ↓
[Support Query: ticket or chat message arrives]
        ↓
[RAG Retrieval: top-k relevant chunks fetched]
        ↓
[Claude Agent: generates response with retrieved context]
        ↓
[Output: answer + source citations + confidence score]
```

### Tech components
- n8n workflow: query orchestration
- Python service: ingestion pipeline + retrieval
- Vector DB: ChromaDB (self-hosted, Docker)
- Claude: answer generation with retrieved context
- Synthetic KB: 20 docs for fictional SaaS product "AcmeCRM"
- NOTE: Claude Cowork generates the synthetic knowledge base documents (Day 8)

### Folder structure to produce
```
project-2-support-chatbot-rag/
├── n8n/
│   └── workflow.json
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── ingestion.py               # Chunk + embed + store
│   ├── retrieval.py               # Vector search + ranking
│   └── agent.py                   # Claude RAG agent
├── tests/
│   ├── conftest.py
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_agent.py
├── data/
│   └── knowledge_base/            # Synthetic docs (Cowork generates)
│       ├── faq.md
│       ├── product_guide.md
│       ├── troubleshooting.md
│       └── [17 more docs]
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md                      # Cowork generates this
```

---

## Project #3 — Document Processing / Invoicing

**Folder:** `project-3-document-processing/`
**Sprint window:** Days 11–14 · Close target: Jul 1
**Hours allocated:** ~17h

### What it does
Extracts structured data from emails or PDFs → registers in system →
routes by document type → generates invoices or summary reports.
Saves hours of manual data entry. Combo: document AI + automation.

### Workflow (end-to-end)
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

### Tech components
- n8n workflow: orchestration + routing
- Python service: PDF extraction + data processing
- Claude: intelligent data extraction from unstructured docs
- PostgreSQL: document registry
- Report generator: PDF output (weasyprint)
- Synthetic data: 10 sample PDFs (fictional invoices + receipts)
- NOTE: Claude Cowork generates the synthetic PDF source documents

### Folder structure to produce
```
project-3-document-processing/
├── n8n/
│   └── workflow.json
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── extractor.py               # Claude-powered data extraction
│   ├── classifier.py              # Document type classification
│   ├── registry.py                # DB registration logic
│   └── report_generator.py        # Invoice/report PDF output
├── tests/
│   ├── conftest.py
│   ├── test_extractor.py
│   ├── test_classifier.py
│   ├── test_registry.py
│   └── test_report_generator.py
├── data/
│   └── sample_documents/          # Synthetic PDFs (Cowork generates)
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md                      # Cowork generates this
```

---

## Reserved — Do Not Touch

- `project-4-content-pipeline/` — Content pipeline + social media automation
- `project-5-client-onboarding/` — Automated client onboarding workflow
