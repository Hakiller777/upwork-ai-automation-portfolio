# upwork-ai-automation-portfolio — Claude Code Context

> This file is auto-read by Claude Code on every session.
> Source of truth for all coding decisions in this repo.

---

## Project Overview

Production-ready AI automation portfolio. Goal: establish a professional
Upwork presence as a Senior AI Automation Specialist and earn the first
3–5 reviews with senior-level portfolio projects.

**Owner:** Hugo — Senior Full Stack Developer, ~8 years experience
**AI Assistant:** Claude (via subscription — no API key)
**Sprint:** Build phase · Jun 24 – Jul 4, 2026 · ~65 total hours

---

## Language Rule (Critical)

- All code, comments, READMEs, docs, variable names → **ENGLISH**
- Hugo communicates in Spanish during sessions — that is fine
- Every deliverable that ships → English only

---

## Repo Structure

```
upwork-ai-automation-portfolio/
├── .claude/                         # Claude Code context (this folder)
│   ├── CLAUDE.md                    # Auto-read master context
│   ├── PROJECTS.md                  # Full specs for all 3 projects
│   ├── STANDARDS.md                 # Code standards + patterns
│   └── SPRINT.md                    # Sprint calendar + current state
├── project-1-lead-generation/
├── project-2-support-chatbot-rag/
├── project-3-document-processing/
├── project-4-content-pipeline/      # Reserved — do not touch
├── project-5-client-onboarding/     # Reserved — do not touch
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Tech Stack

| Component       | Choice                  | Notes                               |
|-----------------|-------------------------|-------------------------------------|
| Automation      | n8n (self-hosted)       | Docker + Railway deploy             |
| Language        | Python 3.11             | Main programming language           |
| AI              | Claude (subscription)   | No external API keys                |
| Containers      | Docker + docker-compose | Base for ALL services               |
| Database        | PostgreSQL              | n8n persistence                     |
| Deploy primary  | Railway                 | Docker-native, ~$5/mo               |
| Deploy fallback | Render (free tier)      | Python services only                |
| Testing         | pytest                  | All projects, no exceptions         |
| Logging         | loguru                  | Structured logs across all projects |

**Never use:** n8n cloud, real API keys from clients, real third-party data, hardcoded secrets.

---

## Active Projects — Priority Order

| # | Project                         | Status          | Target Close |
|---|---------------------------------|-----------------|--------------|
| 1 | Lead Generation + Outreach      | 🔄 Code done, README/Loom/deploy pending | ~~Sáb Jun 27~~ |
| 2 | RAG Support Chatbot             | 🔄 Code done, README/Loom/deploy pending | ~~Mié Jul 1~~ code closed 1-Jul |
| 3 | Document Processing / Invoicing | ⬜ Not started  | Sáb Jul 4    |

Full specs → see PROJECTS.md

---

## Senior Stamp — Required in Every Project

These are NON-NEGOTIABLE. Every project ships with:

- [ ] Unit tests (pytest — happy path + 2 edge cases + 1 error case per module)
- [ ] Error handling (try/except + graceful degradation, never silent failures)
- [ ] Structured logging (loguru — INFO for flow, ERROR for exceptions)
- [ ] Clean architecture (separated concerns: ingestion / processing / output)
- [ ] Architecture diagram (Mermaid in the project README)

---

## Definition of Done — Per Project

A project is NOT complete without ALL five:

1. Documented and commented code (docstrings on every function/class)
2. README in English (architecture + setup + usage + diagram)
3. Loom video showing the workflow running end-to-end
4. Specific deployment guide (step-by-step, Railway + Render)
5. Synthetic sample data included (realistic but 100% fictional)

---

## Critical Rules

1. **Synthetic data only** — never use real third-party data
2. **Simulated integrations** — no real CRM/API client connections
3. **Docker-first** — every service runs in a container
4. **Railway primary, Render fallback** — no other platforms
5. **n8n self-hosted only** — never n8n cloud
6. **No hardcoded secrets** — always .env + .env.example
7. **English everywhere** — code, comments, docs, READMEs
8. **Auto commit + push** — Claude Code commits and pushes to main automatically whenever it considers the work ready, no explicit confirmation needed
9. **Comunicacion_Claude_Project/** — this folder at repo root is the communication bridge from Claude Project (the HQ chat). Hugo drops new files here; Claude Code reads them, applies changes to `.claude/`, commits, and pushes. Never delete this folder.

---

## Roles (Do Not Overlap)

| Tool          | Responsibility                                   |
|---------------|--------------------------------------------------|
| Claude Code   | All coding, Docker, scripts, tests, architecture |
| Claude Cowork | READMEs, deployment guides, knowledge base docs  |
| Project chat  | Decisions, briefs, sprint tracking, prompts      |

When writing code → do not generate READMEs (Cowork's job).
When writing READMEs → do not write code (Code's job).
Exception: inline code blocks inside READMEs are fine.

---

## Deployment Decisions (Already Made)

- **Railway** = primary. Docker-native. Public URL with SSL. ~$5/mo. Hosts n8n + Python apps.
- **Render free** = fallback for Python-only services. Cold start ~1 min after inactivity. Acceptable for demos.
- **Never** n8n cloud official (starts at $24/mo, has execution limits).

---

## Current Sprint State

See SPRINT.md for live day-by-day status.

**✅ As of 2026-07-01 (sesión tarde):** Project #2 (RAG Support Chatbot) construido completo de punta a punta en esta sesión.
- Setup complete (Days 1–2 + Prep #1): docker-compose, Dockerfile, .env.example, README ✅
- Kanban: https://github.com/users/Hakiller777/projects/1
- Project #1 Lead Generation: **código completo** (src/, tests/ con 15 tests, Dockerfile, docker-compose, n8n workflow, Flask API, railway.toml) — hecho en una sola sesión el Jun 24. Falta: README del proyecto, Loom, y confirmar que el deploy en Railway esté realmente arriba.
- Project #2 RAG Support Chatbot: **código completo** (src/config.py, models.py, embeddings.py, ingestion.py, retrieval.py, agent.py, api.py; 16 tests pytest; KB sintética de 20 docs "AcmeCRM"; Dockerfile, docker-compose, n8n/workflow.json, railway.toml) — hecho en una sola sesión el 1-Jul. Verificado end-to-end (ingestion real + query real vía Flask). Falta: README, Loom, confirmar deploy Railway.
- Project #3 Document Processing: **0% — sin archivos**, sin empezar.
- Next: construir Project #3 (extractor, classifier, registry, report_generator + tests + Docker + n8n + Railway) — mismo patrón que #1 y #2. En paralelo, Hugo/Cowork cierran README+Loom+deploy de #1 y #2.
- Ver lista "🚀 NEXT SESSION — START HERE" al tope de SPRINT.md para el detalle exacto de lo pendiente.
