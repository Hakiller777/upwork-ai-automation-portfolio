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
| 3 | Document Processing / Invoicing | 🔄 Code done, README/Loom/deploy pending | ~~Sáb Jul 4~~ code closed 2-Jul |

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

**✅ As of 2026-07-07 (Día 10):** Los 3 proyectos tienen código, tests, README.md y DEPLOYMENT.md 100% completos y verificados. **Lo único que queda en todo el sprint es manual de Hugo: `railway login` + 3 deploys + 3 Looms.**
- Setup complete (Days 1–2 + Prep #1): docker-compose, Dockerfile, .env.example, README ✅
- Kanban: https://github.com/users/Hakiller777/projects/1
- Project #1 Lead Generation: **código + README + DEPLOYMENT.md completos** (src/, tests/ con 26 tests, Dockerfile, docker-compose, n8n workflow, Flask API, railway.toml) — hecho el Jun 24, README+DEPLOYMENT commiteados en `4b4cb48`. Falta: Loom + confirmar deploy Railway (Hugo).
- Project #2 RAG Support Chatbot: **código + README + DEPLOYMENT.md completos** (src/config.py, models.py, embeddings.py, ingestion.py, retrieval.py, agent.py, api.py; 16/16 tests pytest re-verificados en vivo 2026-07-07; KB sintética de 20 docs "AcmeCRM"; Dockerfile, docker-compose, n8n/workflow.json, railway.toml) — código hecho el 1-Jul, README el 6-Jul, DEPLOYMENT.md el 7-Jul. Falta: Loom + deploy Railway (Hugo).
- Project #3 Document Processing: **código + README + DEPLOYMENT.md completos** (src/config.py, models.py, extractor.py con interfaz pluggable `DocumentExtractor` — regex determinístico por defecto + Claude API documentado sin wire-up, classifier.py, registry.py con SQLite, report_generator.py, pipeline.py, api.py; 17/17 tests pytest re-verificados en vivo 2026-07-07; 10 documentos sintéticos: 4 PDFs reales + 6 emails simulados JSON; Dockerfile, docker-compose, n8n/workflow.json, railway.toml) — código hecho el 2-Jul, README el 6-Jul, DEPLOYMENT.md el 7-Jul. Falta: Loom + deploy Railway (Hugo).
- Next: no queda build de código pendiente en el sprint. El deploy real quedó bloqueado en `railway login` (requiere OAuth interactivo con la cuenta de Hugo — no automatizable); una vez logueado, `railway link && railway up` por carpeta de proyecto según cada DEPLOYMENT.md.
- Ver lista "🚀 NEXT SESSION — START HERE" al tope de SPRINT.md para el detalle exacto de lo pendiente.
