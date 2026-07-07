# Sprint State

> Sprint recalibrado — build arranca Jun 24, 2026 · ~65 total hours
> Recalibraciones: Jun 15, Jun 17, Jun 24 (inicio build efectivo)

---

## Current Status

| Indicator           | Value                                                              |
|---------------------|--------------------------------------------------------------------|
| Current day         | **Mar Jul 7, 2026**                                                |
| Projects done       | **0 / 3** (code + docs ✅ para los 3 — Loom video ⏳ pendiente para los 3) |
| Deploy status       | **✅ Los 3 servicios live en Railway, health check 200 en los 3** |
| Active project      | Pendiente: grabar Loom de #1, #2 y #3                              |
| Next milestone      | Loom videos → **CIERRE de los 3 proyectos**                        |
| Active blockers     | None (Railway free-plan limit resuelto — ver Key Decisions Log)   |

---

## Completed Setup (Before Jun 24)

| Day     | Date       | Focus                                               | Status  |
|---------|------------|-----------------------------------------------------|---------|
| 1       | Vie Jun 12 | Setup: repo + 5-folder structure + Kanban          | ✅ Done |
| 2       | Vie Jun 12 | Setup: docker-compose + Dockerfile + .env + README | ✅ Done |
| Prep #1 | Jun 17–19  | Brief de arquitectura + datos sintéticos Proyecto 1 | ✅ Done |

---

## Day-by-Day Calendar (Build — desde Jun 24)

| Day | Date        | Hours | Focus                                                               | Profile (parallel)         | Status       |
|-----|-------------|-------|---------------------------------------------------------------------|----------------------------|--------------|
| 1   | Mié Jun 24  | 3h    | **#1** Architecture + core src/ + synthetic data CSV                | —                          | ✅ Done      |
| 2   | Jue Jun 25  | 3h    | **#1** scoring.py + outreach.py + pipeline.py                       | —                          | ✅ Done      |
| 3   | Vie Jun 26  | 3h    | **#1** tests (pytest) + Dockerfile + docker-compose                 | —                          | ✅ Done      |
| 4   | Sáb Jun 27  | 8h    | **#1** n8n workflow + Flask API + railway.toml → **code complete** | —                          | ✅ Done      |
| 5   | Dom Jun 28  | 8h    | **#2** Architecture + ingestion + ChromaDB + KB sintética          | LinkedIn: headline + photo | 🔄 Today     |
| 6   | Lun Jun 29  | 3h    | **#2** agent logic + retrieval                                      | —                          | ⬜           |
| 7   | Mar Jun 30  | 3h    | **#2** tests + error handling + logging                             | LinkedIn: About            | ⬜           |
| 8   | Mié Jul 1   | 3h    | **#2** deploy Railway + Loom → **CLOSE #2**                        | —                          | ⬜           |
| 9   | Jue Jul 2   | 3h    | **#3** Architecture + extractor + classifier + datos                | Upwork: title + overview   | ⬜           |
| 10  | Vie Jul 3   | 3h    | **#3** registry + report generator + n8n workflow                   | —                          | ⬜           |
| 11  | Sáb Jul 4   | 8h    | **#3** tests + deploy + Loom → **CLOSE #3** + polish final         | Upwork: portfolio 3 videos | ⬜           |

---

## Project Close Targets

| Project                         | Close Target                         |
|---------------------------------|--------------------------------------|
| #1 Lead Generation + Outreach   | ~~Sáb Jun 27~~ code ✅ · Loom ⏳     |
| #2 RAG Support Chatbot          | **Mié Jul 1**                        |
| #3 Document Processing          | **Sáb Jul 4**                        |

---

## Completed Milestones

- [x] Day 0 (Jun 10) — Tracking system built, roles defined
- [x] Day 1 (Jun 12) — Repo created, 5-folder structure pushed, Kanban live
- [x] Day 2 (Jun 12) — docker-compose.yml base, Dockerfile, .env.example, README
- [x] Prep #1 (Jun 17–19) — Architecture brief + synthetic data specs
- [x] Jun 24 — Sprint recalibrado definitivo
- [x] Build Day 1 (Jun 24) — models + config + enrichment + skeletons + 50 leads CSV
- [x] Build Day 2 (Jun 25) — scoring + outreach + pipeline (end-to-end funcional)
- [x] Build Day 3 (Jun 26) — pytest suite (15 tests) + Dockerfile + docker-compose
- [x] Build Day 4 (Jun 27) — n8n workflow + Flask API + railway.toml → Project #1 code complete
- [x] Jul 7 — Project #2 y #3 code + tests + docs completos (ver commits previos)
- [x] Jul 7 — **Deploy Railway de los 3 proyectos**, dominio público + health check 200 en los 3, README actualizado con URL real

---

## Key Decisions Log

| Date   | Decision                                                                  |
|--------|--------------------------------------------------------------------------|
| Jun 10 | One chat per day, one bitacora per day as MD context file                 |
| Jun 10 | Cowork = docs/READMEs, Code = coding, Project chat = HQ                  |
| Jun 12 | GitHub CLI (gh) adopted as standard for GitHub operations                 |
| Jun 12 | Kanban cards created as drafts (not issues) — faster                     |
| Jun 15 | Sprint redistribuido                                                       |
| Jun 17 | Prep #1 insertado antes del build                                          |
| Jun 24 | Sprint recalibrado definitivo — build arranca Jun 24 (Mié), cierre Jul 4 |
| Jun 24 | enrichment.py implementado completo (rule-based) en Día 1                |
| Jun 25 | pipeline.py agregado como runner end-to-end                               |
| Jun 26 | pytest suite: 15 tests cubriendo happy path + edge cases + error cases    |
| Jun 27 | Flask API (src/api.py) agregado — HTTP layer para integración con n8n    |
| Jul 7  | Deploy Railway: plan Free bloqueó creación de proyecto nuevo (resource limit) — se reusaron 2 proyectos vacíos preexistentes para #1/#2 y #3 se desplegó como segundo servicio dentro del mismo proyecto que #1 |
| Jul 7  | Pendiente antes de cerrar los 3 proyectos: grabar y subir Loom video de cada uno |
