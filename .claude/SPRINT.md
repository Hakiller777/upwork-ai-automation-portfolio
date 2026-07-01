# Sprint State

> Sprint recalibrado — build arranca Jun 24, 2026 · ~65 total hours
> Recalibraciones: Jun 15, Jun 17, Jun 24 (inicio build efectivo)
> **⚠️ Actualizado 2026-07-01:** sin actividad en el repo desde Jun 24 (Build Day 4). El plan tenía Días 5–8 (Jun 28–Jul 1, Project #2 completo) para hoy — no se ejecutaron.

---

## 🚀 NEXT SESSION — START HERE

Sesión cerrada el 2026-07-01 con esta lista acordada como punto de partida. Objetivo: cerrar todo esto en la próxima sesión para llegar al 2-Jul alineados con el Día 9 del calendario (Project #3).

**Project #1 — wrap-up (código ya completo, falta cerrar):**
- [ ] README.md de `project-1-lead-generation/` (arquitectura + setup + uso + diagrama Mermaid)
- [ ] Confirmar/ejecutar deploy real en Railway (Hugo)
- [ ] Grabar Loom del flujo end-to-end (Hugo)

**Project #2 — RAG Support Chatbot (0% → build completo desde cero):**
- [ ] `src/config.py`, `src/models.py` — arquitectura base
- [ ] `src/ingestion.py` — chunking + embeddings + carga a ChromaDB
- [ ] `src/retrieval.py` — búsqueda vectorial + ranking
- [ ] `src/agent.py` — agente Claude con contexto RAG
- [ ] Base de conocimiento sintética (20 docs de "AcmeCRM": faq.md, product_guide.md, troubleshooting.md + 17 más) — normalmente de Cowork, redactar mínimo viable si bloquea
- [ ] `tests/` pytest (ingestion, retrieval, agent) — happy path + edge cases + error case
- [ ] Dockerfile + docker-compose + servicio ChromaDB
- [ ] `n8n/workflow.json` — orquestación de queries
- [ ] `railway.toml` / deploy config
- [ ] README.md
- [ ] Deploy real en Railway (Hugo)
- [ ] Loom del flujo end-to-end (Hugo)

**Nota de alcance:** esto representa ~17-20h de trabajo (todo lo que estaba repartido en Días 5-8), no las 3h nominales del Día 8. Si no cierra completo en una sesión, lo que quede pendiente se termina antes de arrancar Project #3 — no se acumula como atraso nuevo.

---

## Current Status

| Indicator           | Value                                                              |
|---------------------|--------------------------------------------------------------------|
| Current real date   | **Wed Jul 1, 2026**                                                |
| Last real commit    | **Jun 24** (Build Days 1–4, todo en una sola sesión)               |
| Days idle           | **7 días sin commits** (Jun 25 – Jul 1)                             |
| Hours consumed      | **~23 / 65 h** (self-reported, sin cambios desde Jun 24)           |
| Projects done       | **0 / 3** — Project #1: código completo ✅, falta README + Loom + confirmar deploy Railway |
| Project #2 (RAG)    | **0% — sin archivos** (plan esperaba Días 5–8 completos hoy)       |
| Project #3 (Docs)   | **0% — sin archivos**                                              |
| Next milestone (plan original) | Hoy (Jul 1) = cierre Project #2 — no alcanzado           |
| Active blockers     | **Sprint frenado desde Jun 24** — necesita decisión de replanificación (ver Pending Items) |

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
| 2   | Jue Jun 25  | 3h    | **#1** scoring.py + outreach.py + pipeline.py                       | —                          | ✅ Done (real: hecho el mismo Jun 24) |
| 3   | Vie Jun 26  | 3h    | **#1** tests (pytest) + Dockerfile + docker-compose                 | —                          | ✅ Done (real: hecho el mismo Jun 24) |
| 4   | Sáb Jun 27  | 8h    | **#1** n8n workflow + Flask API + railway.toml → **code complete** | —                          | ✅ Done (real: hecho el mismo Jun 24) |
| 5   | Dom Jun 28  | 8h    | **#2** Architecture + ingestion + ChromaDB + KB sintética          | LinkedIn: headline + photo | ⬜ Missed — sin archivos en project-2 |
| 6   | Lun Jun 29  | 3h    | **#2** agent logic + retrieval                                      | —                          | ⬜ Missed   |
| 7   | Mar Jun 30  | 3h    | **#2** tests + error handling + logging                             | LinkedIn: About            | ⬜ Missed   |
| 8   | Mié Jul 1   | 3h    | **#2** deploy Railway + Loom → **CLOSE #2**                        | —                          | ⬜ **Hoy — Project #2 en 0%, no se puede cerrar** |
| 9   | Jue Jul 2   | 3h    | **#3** Architecture + extractor + classifier + datos                | Upwork: title + overview   | ⬜           |
| 10  | Vie Jul 3   | 3h    | **#3** registry + report generator + n8n workflow                   | —                          | ⬜           |
| 11  | Sáb Jul 4   | 8h    | **#3** tests + deploy + Loom → **CLOSE #3** + polish final         | Upwork: portfolio 3 videos | ⬜           |

**Nota (2026-07-01):** los "Días 2–4" del build quedaron marcados como fechas Jun 25–27 pero en la práctica todo el código de Project #1 (arquitectura, scoring, outreach, pipeline, 15 tests, Docker, n8n workflow, Flask API, railway.toml) se hizo en una sola sesión el **Jun 24**. Desde entonces, **7 días calendario sin ningún commit** — Project #2 (RAG) sigue en 0%, sin un solo archivo en `project-2-support-chatbot-rag/` más allá del README placeholder. El plan esperaba tener Project #2 cerrado hoy (Jul 1); en cambio no se empezó.

---

## Project Close Targets

| Project                         | Close Target                         |
|---------------------------------|--------------------------------------|
| #1 Lead Generation + Outreach   | ~~Sáb Jun 27~~ code ✅ · falta README + Loom + confirmar deploy Railway |
| #2 RAG Support Chatbot          | ~~Mié Jul 1 (hoy)~~ **incumplido — 0% avance** |
| #3 Document Processing          | **Sáb Jul 4** — en riesgo alto        |

---

## Pending Items (real, 2026-07-01)

| # | Item                                                              | Deadline      | Status      |
|---|--------------------------------------------------------------------|---------------|-------------|
| 1 | Project #1 — escribir README (arquitectura + setup + uso + diagrama Mermaid) | Urgente | ⬜ Open |
| 2 | Project #1 — grabar Loom del flujo end-to-end                     | Urgente       | ⬜ Open     |
| 3 | Project #1 — confirmar deploy real en Railway (no verificable desde el repo) | Urgente | ⬜ Open |
| 4 | Project #2 — no iniciado, plan original lo daba por cerrado hoy    | Vencido       | 🚩 Blocking |
| 5 | Decidir: replanificar calendario desde Jul 1, o recortar alcance (ej. 2 proyectos pulidos en vez de 3) antes de seguir | Urgente — sprint cierra Jul 4 | 🚩 Blocking |

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
