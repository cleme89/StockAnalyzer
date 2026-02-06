# StockAnalyzer

Progetto demo: backend in `FastAPI` per fornire API di analisi su azioni/ETF.

## Quick start (dev)

### Windows PowerShell - Avvia tutto in automatico:
```powershell
.\dev.ps1
```
Apre due finestre: una col backend, una col frontend dev.

### Oppure sep aratamente:

**Backend (terminal 1):**
```powershell
cd backend
.\run.ps1
# Backend: http://127.0.0.1:8000
# Swagger: http://127.0.0.1:8000/docs
```

**Frontend (terminal 2):**
```powershell
cd frontend
.\run.ps1
# Frontend: http://localhost:4200
```

## Quick start (Docker)

```bash
docker compose up --build
# backend: http://localhost:8000
# frontend: http://localhost
```

## Endpoints

- `GET /health`
- `GET /quote/{symbol}`
- `POST /analyze` body `{ "symbol":"AAPL", "start":"2025-01-01", "end":"2025-02-01", "window":20 }`
