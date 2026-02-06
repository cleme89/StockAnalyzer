# StockAnalyzer

Progetto demo: backend in `FastAPI` per fornire API di analisi su azioni/ETF.

Quick start (virtualenv):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

Quick start (docker):

```bash
docker compose up --build
# backend sarà su http://localhost:8000
# frontend sarà su http://localhost (porta 80)
```

Endpoints utili:
- `GET /health`
- `GET /quote/{symbol}`
- `POST /analyze` body `{ "symbol":"AAPL", "start":"2025-01-01", "end":"2025-02-01", "window":20 }`
