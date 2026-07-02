# Sprint State

> Sprint recalibrado — build arranca Jun 24, 2026 · ~65 total hours
> Recalibraciones: Jun 15, Jun 17, Jun 24 (inicio build efectivo)
> **✅ Actualizado 2026-07-02:** Project #3 (Document Processing) construido completo de punta a punta en esta sesión — código, tests, datos sintéticos, Docker, n8n, Railway config. Con esto, **los 3 proyectos tienen código 100% completo**. Falta solo README + deploy real + Loom (Hugo/Cowork) en los 3.

---

## 🚀 NEXT SESSION — START HERE

**Los 3 proyectos tienen código completo. Queda solo el wrap-up manual (Hugo/Cowork), en paralelo por proyecto:**

**Project #1 — wrap-up:**
- [ ] README.md de `project-1-lead-generation/` (arquitectura + setup + uso + diagrama Mermaid) — Cowork
- [ ] Confirmar/ejecutar deploy real en Railway (Hugo)
- [ ] Grabar Loom del flujo end-to-end (Hugo)

**Project #2 — wrap-up:**
- [ ] README.md — Cowork
- [ ] Deploy real en Railway (Hugo)
- [ ] Loom del flujo end-to-end (Hugo)

**Project #3 — wrap-up:**
- [ ] README.md de `project-3-document-processing/` (arquitectura + setup + uso + diagrama Mermaid) — Cowork
- [ ] Deploy real en Railway (Hugo)
- [ ] Loom del flujo end-to-end (Hugo)
- [ ] Nota para Cowork: dataset sintético quedó en 4 PDFs reales (reportlab) + 6 emails simulados (JSON) = 10 documentos totales, no 10 PDFs puros — simplificación de tiempo, documentada abajo. Ampliar a más PDFs reales es opcional, no bloqueante.

**Nota:** con los 3 proyectos de código cerrado, el sprint termina Jul 4 con solo wrap-up manual (READMEs/Looms/deploys Railway) pendiente — no queda más build de Claude Code en el alcance actual.

**Sesión cerrada 2026-07-02 — próxima sesión arranca con el wrap-up manual de los 3 proyectos (Hugo/Cowork). Si aparece más trabajo de código, sería sobre #4/#5 (reservados, no tocar aún) o fixes puntuales.**

---

## Current Status

| Indicator           | Value                                                              |
|---------------------|--------------------------------------------------------------------|
| Current real date   | **Thu Jul 2, 2026**                                                |
| Last real commit    | **Jul 2** (Project #3 build — código completo en esta sesión)      |
| Hours consumed      | **~23 / 65 h** (self-reported; no incluye la sesión de hoy)        |
| Projects done       | **0 / 3 cerrados** — #1, #2 y #3: código completo ✅, falta README + Loom + confirmar deploy Railway en los 3 |
| Project #3 (Docs)   | **Código completo** — src/ (extractor pluggable, classifier, registry SQLite, report_generator, pipeline, api), tests/ (17 tests), 10 docs sintéticos (4 PDF + 6 email JSON), Dockerfile, docker-compose, n8n workflow, railway.toml |
| Next milestone      | Cerrar #1, #2 y #3 (README/Loom/deploy — Cowork + Hugo). No queda build de código pendiente en el alcance actual |
| Active blockers     | Ninguno de código — quedan tareas manuales (Loom, deploy Railway) fuera del alcance de Claude Code |

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
| 5   | Dom Jun 28  | 8h    | **#2** Architecture + ingestion + ChromaDB + KB sintética          | LinkedIn: headline + photo | ✅ Done (real: hecho el 1-Jul) |
| 6   | Lun Jun 29  | 3h    | **#2** agent logic + retrieval                                      | —                          | ✅ Done (real: hecho el 1-Jul) |
| 7   | Mar Jun 30  | 3h    | **#2** tests + error handling + logging                             | LinkedIn: About            | ✅ Done (real: hecho el 1-Jul) |
| 8   | Mié Jul 1   | 3h    | **#2** deploy Railway + Loom → **CLOSE #2**                        | —                          | 🔄 Código ✅ — falta deploy + Loom (Hugo) |
| 9   | Jue Jul 2   | 3h    | **#3** Architecture + extractor + classifier + datos                | Upwork: title + overview   | ✅ Done (código completo, ver nota) |
| 10  | Vie Jul 3   | 3h    | **#3** registry + report generator + n8n workflow                   | —                          | ✅ Done (real: hecho el mismo Jul 2) |
| 11  | Sáb Jul 4   | 8h    | **#3** tests + deploy + Loom → **CLOSE #3** + polish final         | Upwork: portfolio 3 videos | 🔄 Tests ✅ (real: hecho el mismo Jul 2) — falta deploy + Loom (Hugo) |

**Nota (2026-07-01):** Project #2 (RAG Support Chatbot) se construyó completo en la sesión de la tarde del 1-Jul: `src/config.py`, `models.py`, `embeddings.py` (vectorizer hashing determinístico, offline), `ingestion.py`, `retrieval.py`, `agent.py` (generación simulada tipo Claude, mismo patrón que scoring.py de Project #1), `api.py` (Flask), knowledge base sintética de 20 docs para "AcmeCRM", 16 tests pytest (todos pasando), Dockerfile, docker-compose.yml, n8n/workflow.json, railway.toml. Verificado end-to-end: ingestion real (20 docs → 60 chunks) + query real vía Flask API con respuesta y citas correctas. Docker build no se pudo verificar en esta sesión (Docker Desktop no estaba corriendo) pero el Dockerfile replica el patrón ya probado de Project #1.

**Nota (2026-07-02):** Project #3 (Document Processing) se construyó completo en esta sesión: `src/config.py`, `models.py`, `extractor.py` (interfaz pluggable `DocumentExtractor` — `RegexDocumentExtractor` determinístico/offline por defecto + `ClaudeDocumentExtractor` documentado como path de producción, seleccionable por `EXTRACTION_BACKEND`), `classifier.py` (detección de tipo + validación de campos mínimos), `registry.py` (persistencia SQLite con query por status/tipo/fecha), `report_generator.py` (reporte JSON por defecto, PDF opcional vía reportlab), `pipeline.py` (orquesta extract→classify→register→report con manejo de errores por etapa, un documento mal formado no tumba el batch), `api.py` (Flask: /health, /process, /documents, /documents/<id>). 17 tests pytest (todos pasando). Datos sintéticos: 4 PDFs reales (generados con reportlab, parseados con pypdf) + 6 emails simulados (JSON con campo `body`) = 10 documentos, mezclando invoices/receipts/purchase orders válidos con un documento incompleto y un email no relacionado (para probar `NEEDS_REVIEW`). Verificado end-to-end: pipeline CLI real sobre los 10 documentos (8 reported, 2 needs_review, 0 failed) + Flask API real (/health, /process, /documents con filtros, /documents/<id>). docker-compose de los 3 proyectos + el root validado sin conflictos de puerto (8000/8001/8002) sobre la red compartida `automation-net`. Simplificación de tiempo: dataset mixto PDF+email en vez de 10 PDFs puros — documentado como pendiente opcional para Cowork.

---

## Project Close Targets

| Project                         | Close Target                         |
|---------------------------------|--------------------------------------|
| #1 Lead Generation + Outreach   | ~~Sáb Jun 27~~ code ✅ · falta README + Loom + confirmar deploy Railway |
| #2 RAG Support Chatbot          | ~~Mié Jul 1~~ code ✅ (1-Jul) · falta README + Loom + confirmar deploy Railway |
| #3 Document Processing          | ~~Sáb Jul 4~~ code ✅ (2-Jul) · falta README + Loom + confirmar deploy Railway |

---

## Pending Items (real, 2026-07-02)

| # | Item                                                              | Deadline      | Status      |
|---|--------------------------------------------------------------------|---------------|-------------|
| 1 | Project #1 — escribir README (arquitectura + setup + uso + diagrama Mermaid) | Urgente | ⬜ Open |
| 2 | Project #1 — grabar Loom del flujo end-to-end                     | Urgente       | ⬜ Open     |
| 3 | Project #1 — confirmar deploy real en Railway (no verificable desde el repo) | Urgente | ⬜ Open |
| 4 | Project #2 — escribir README (arquitectura + setup + uso + diagrama Mermaid) | Urgente | ⬜ Open |
| 5 | Project #2 — grabar Loom del flujo end-to-end                     | Urgente       | ⬜ Open     |
| 6 | Project #2 — confirmar deploy real en Railway (no verificable desde el repo) | Urgente | ⬜ Open |
| 7 | Project #3 — escribir README (arquitectura + setup + uso + diagrama Mermaid) | Urgente | ⬜ Open |
| 8 | Project #3 — grabar Loom del flujo end-to-end                     | Urgente       | ⬜ Open     |
| 9 | Project #3 — confirmar deploy real en Railway (no verificable desde el repo) | Urgente | ⬜ Open |

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
- [x] Build Day 5-8 (real: Jul 1) — Project #2 RAG chatbot: ingestion + retrieval + agent + KB sintética (20 docs) + 16 tests + Docker + n8n + railway.toml → Project #2 code complete
- [x] Build Day 9-11 (real: Jul 2) — Project #3 Document Processing: extractor (pluggable) + classifier + registry SQLite + report_generator + pipeline + 17 tests + 10 docs sintéticos (4 PDF + 6 email JSON) + Docker + n8n + railway.toml → Project #3 code complete — **los 3 proyectos tienen código cerrado**

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
| Jul 1  | Project #2: embeddings implementados con un vectorizer hashing determinístico propio (no modelo externo ni API) para mantener el demo 100% offline y sin dependencias pesadas — swap documentado en código para producción |
| Jul 2  | Project #3: extracción vía interfaz pluggable `DocumentExtractor` (regex determinístico por defecto, Claude API documentado pero sin wire-up) — mismo patrón de "mock swappable por env var" que scoring.py (#1) y embeddings.py (#2) |
| Jul 2  | Project #3: registro de documentos en SQLite (no JSON plano) para permitir queries indexadas por status/tipo/fecha sin cargar todo en memoria |
| Jul 2  | Project #3: dataset sintético mixto (4 PDFs reales via reportlab + 6 emails simulados JSON) en vez de 10 PDFs puros, para cubrir ambos canales de entrada ("PDFs o emails") sin bloquear el sprint en generación de PDFs |
