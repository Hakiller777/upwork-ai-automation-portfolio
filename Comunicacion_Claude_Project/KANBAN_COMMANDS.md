# Kanban Update Commands — Sprint Jun 16–25

> Prompt único para Claude Code: al cerrar cada día, ejecutar los comandos
> de esta sección para mantener el tablero sincronizado con el trabajo real.
>
> Kanban: https://github.com/users/Hakiller777/projects/1
> Método: `gh project item-edit` via PowerShell (no browser needed)

---

## Constants (no tocar)

```powershell
$PROJ    = "PVT_kwHOB2cu8c4Baerq"
$FIELD   = "PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ"
$HECHO   = "98236657"      # ✅ Hecho
$PROGRES = "47fc9ee4"      # 🔄 En progreso
$BACKLOG = "f75ad846"      # 📋 Backlog
```

---

## Item IDs — Referencia completa

| ID                              | Tarjeta                                         | Estado actual  |
|---------------------------------|-------------------------------------------------|----------------|
| PVTI_lAHOB2cu8c4Baerqzgv11AQ   | Día 1 — Repo + Estructura + Kanban              | ✅ Hecho       |
| PVTI_lAHOB2cu8c4BaerqzgvjxPo   | Día 2 — Docker base + Railway + README          | ✅ Hecho       |
| PVTI_lAHOB2cu8c4Baerqzgvjzn8   | #1 — Arquitectura + nucleo + datos sint.        | 🔄 En progreso |
| PVTI_lAHOB2cu8c4Baerqzgvjz2s   | #1 — Logica + tests + errores + logging         | 🔄 En progreso |
| PVTI_lAHOB2cu8c4Baerqzgvjz3Q   | #1 — README + diagrama de arquitectura          | 🔄 En progreso |
| PVTI_lAHOB2cu8c4Baerqzgvjz34   | #1 — Deploy Railway + Loom — CIERRE             | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz40   | #2 — Arquitectura + setup RAG/vector            | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz5g   | #2 — Ingestion docs + base de conocimiento      | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz6U   | #2 — Logica del agente + errores                | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz7U   | #2 — Terminar + tests + deploy + Loom — CIERRE  | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz8Q   | #3 — Arquitectura + extraccion + datos + nucleo | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz80   | #3 — Ruteo + generacion facturas/reportes       | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz9o   | #3 — Tests + logging + errores                  | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvjz-Y   | #3 — README + diagrama + deploy + Loom — CIERRE | 📋 Backlog     |
| PVTI_lAHOB2cu8c4Baerqzgvj0Ao   | Dia 15 — Pulido final + checklist               | 📋 Backlog     |

---

## Comandos por día

### FIN DEL DÍA 3 — Lun Jun 16
> Cierra: #1 Arquitectura. Nada nuevo a En progreso (ya están las otras 2 tarjetas).

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjzn8 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #1 Arquitectura → Hecho"
```

---

### FIN DEL DÍA 4 — Mar Jun 17
> Cierra: #1 Logica + tests.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz2s --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #1 Logica + tests → Hecho"
```

---

### FIN DEL DÍA 5 — Mié Jun 18
> Cierra: #1 README + diagrama. Mueve a En progreso: #1 Deploy.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz3Q --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #1 README + diagrama → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz34 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #1 Deploy + Loom → En progreso"
```

---

### FIN DEL DÍA 6 — Jue Jun 19 — CIERRE PROJECT #1
> Cierra: #1 Deploy + Loom. Mueve a En progreso: #2 Arquitectura.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz34 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #1 Deploy + Loom → Hecho  *** CIERRE PROJECT #1 ***"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz40 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #2 Arquitectura → En progreso"
```

---

### FIN DEL DÍA 7 — Vie Jun 20
> Cierra: #2 Arquitectura. Mueve a En progreso: #2 Ingestion + #2 Agente.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz40 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #2 Arquitectura → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz5g --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #2 Ingestion → En progreso"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz6U --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #2 Agente → En progreso"
```

---

### FIN DEL DÍA 8 — Sáb Jun 21
> Cierra: #2 Ingestion + #2 Agente. Mueve a En progreso: #2 Terminar.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz5g --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #2 Ingestion → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz6U --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #2 Agente → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz7U --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #2 Terminar + deploy → En progreso"
```

---

### FIN DEL DÍA 9 — Dom Jun 22 — CIERRE PROJECT #2
> Cierra: #2 Terminar. Mueve a En progreso: #3 Arquitectura.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz7U --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #2 Terminar + deploy → Hecho  *** CIERRE PROJECT #2 ***"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz8Q --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #3 Arquitectura → En progreso"
```

---

### FIN DEL DÍA 10 — Lun Jun 23
> Cierra: #3 Arquitectura. Mueve a En progreso: #3 Ruteo + #3 Tests.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz8Q --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #3 Arquitectura → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz80 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #3 Ruteo → En progreso"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz9o --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #3 Tests + logging → En progreso"
```

---

### FIN DEL DÍA 11 — Mar Jun 24
> Cierra: #3 Ruteo + #3 Tests. Mueve a En progreso: #3 README + deploy.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz80 --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #3 Ruteo → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz9o --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #3 Tests + logging → Hecho"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz-Y --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 47fc9ee4
Write-Host "🔄 #3 README + deploy → En progreso"
```

---

### FIN DEL DÍA 12 — Mié Jun 25 — CIERRE PROJECT #3 + SPRINT COMPLETO
> Cierra todo. Sprint terminado.

```powershell
gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvjz-Y --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ #3 README + deploy → Hecho  *** CIERRE PROJECT #3 ***"

gh project item-edit --project-id PVT_kwHOB2cu8c4Baerq --id PVTI_lAHOB2cu8c4Baerqzgvj0Ao --field-id PVTSSF_lAHOB2cu8c4BaerqzhVWBAQ --single-select-option-id 98236657
Write-Host "✅ Día 15 Pulido final → Hecho  *** SPRINT COMPLETO ***"
```

---

## Verificación rápida (cualquier momento)

```powershell
gh project item-list 1 --owner Hakiller777 --format json |
  ConvertFrom-Json |
  Select-Object -ExpandProperty items |
  Select-Object status, title |
  Format-Table -AutoSize
```
