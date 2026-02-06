# Script per avviare il frontend StockAnalyzer
# Avvia come: .\run.ps1

Write-Host "Avvio StockAnalyzer Frontend (dev)..." -ForegroundColor Cyan

# Controlla se node_modules esiste
if (-Not (Test-Path ".\node_modules")) {
    Write-Host "Installazione dipendenze..." -ForegroundColor Yellow
    npm install
}

Write-Host "Dev server avviato su http://localhost:4200" -ForegroundColor Green
Write-Host "Assicurati che il backend sia in esecuzione su http://127.0.0.1:8000" -ForegroundColor Yellow
Write-Host ""

# Avvia il dev server con proxy
ng serve --host 0.0.0.0 --proxy-config proxy.conf.json
