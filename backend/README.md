# Backend (FastAPI)

Run local (virtualenv):

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Run with Docker:

```bash
docker build -t stockanalyzer-backend .
docker run -p 8000:8000 stockanalyzer-backend
```

If you use the provided `docker-compose.yml`, run from repository root:

```bash
docker compose up --build
# backend: http://localhost:8000
# frontend: http://localhost
```
