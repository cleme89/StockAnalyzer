# Script per avviare TUTTO (backend + frontend dev in parallelo)
# Avvia come: .\dev.ps1

Write-Host "Avvio StockAnalyzer (Backend + Frontend)..." -ForegroundColor Cyan
Write-Host ""

# Avvia il backend in background
Write-Host "Avvio backend..." -ForegroundColor Yellow
$backendPath = Join-Path -Path (Get-Location) -ChildPath "backend"
Start-Process powershell -ArgumentList "-NoExit -Command `"Set-Location '$backendPath'; .\run.ps1`"" -WindowStyle Normal

# Attendi un momento che il backend sia pronto
Start-Sleep -Seconds 3

# Avvia il frontend
Write-Host "Avvio frontend..." -ForegroundColor Yellow
$frontendPath = Join-Path -Path (Get-Location) -ChildPath "frontend"
Set-Location $frontendPath
.\run.ps1
