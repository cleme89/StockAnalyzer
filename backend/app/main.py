from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from . import analysis

app = FastAPI(title="StockAnalyzer API")

# Enable CORS for development and deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    symbol: str
    start: str | None = None
    end: str | None = None
    window: int | None = 20


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/quote/{symbol}")
async def quote(symbol: str):
    try:
        q = analysis.get_latest_quote(symbol)
        return q
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    try:
        result = analysis.simple_moving_average(req.symbol, req.start, req.end, req.window)
        return {"symbol": req.symbol.upper(), "sma": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/usa/winners")
async def usa_winners():
    try:
        result = analysis.get_market_winners("USA")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/usa/losers")
async def usa_losers():
    try:
        result = analysis.get_market_losers("USA")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/milan/winners")
async def milan_winners():
    try:
        result = analysis.get_market_winners("MILAN")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/milan/losers")
async def milan_losers():
    try:
        result = analysis.get_market_losers("MILAN")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/switzerland/winners")
async def switzerland_winners():
    try:
        result = analysis.get_market_winners("SWITZERLAND")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/markets/switzerland/losers")
async def switzerland_losers():
    try:
        result = analysis.get_market_losers("SWITZERLAND")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

