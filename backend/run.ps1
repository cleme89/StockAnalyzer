# Script per avviare il backend StockAnalyzer
# Avvia come: .\run.ps1

Write-Host "Avvio StockAnalyzer Backend..." -ForegroundColor Cyan

# Nascondi il messaggio di attivazione
$env:VIRTUAL_ENV_DISABLE_PROMPT = 1

# Controlla se le dipendenze sono già installate
if (-Not (Test-Path ".\venv\Scripts\python.exe")) {
    Write-Host "Creazione virtualenv..." -ForegroundColor Yellow
    py -m venv venv
}

Write-Host "Installazione dipendenze..." -ForegroundColor Yellow
py -m pip install -q -r requirements.txt

Write-Host "Backend avviato su http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "Swagger UI: http://127.0.0.1:8000/docs" -ForegroundColor Green
Write-Host ""

# Avvia il server
py -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
