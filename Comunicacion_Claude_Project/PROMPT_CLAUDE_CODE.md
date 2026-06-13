# Prompt para Claude Code — Crear estructura .claude en el repo

Pegá esto directamente en Claude Code (PowerShell o terminal del repo):

---

## PROMPT

```
I need you to create the .claude context folder in the root of this repo.
This folder gives Claude Code full context about the project on every session.

Create the following structure:

.claude/
├── CLAUDE.md      ← main context (auto-read by Claude Code)
├── PROJECTS.md    ← full specs for all 3 portfolio projects
├── STANDARDS.md   ← code standards, patterns, senior stamp requirements
└── SPRINT.md      ← sprint calendar and current state

Use the exact content from the 4 markdown files I will provide.

After creating the files:
1. Stage all 4 files: git add .claude/
2. Commit: git commit -m "chore: add .claude context folder for Claude Code sessions"
3. Push: git push origin main

Confirm each file was created and the push succeeded.
```

---

## Cómo usarlo

1. Abrís Claude Code en VSCode o PowerShell
2. Pegás el prompt de arriba
3. Adjuntás / pegás el contenido de los 4 archivos MD que te pasé
4. Claude Code crea la estructura, hace el commit y pushea

## Verificación

Después del push, confirmá en GitHub que exista:
https://github.com/Hakiller777/upwork-ai-automation-portfolio/tree/main/.claude

Los 4 archivos deben aparecer ahí.
