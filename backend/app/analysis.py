import pandas as pd
import yfinance as yf
from datetime import datetime

# Mock data for markets (replace with real API calls when needed)
MOCK_USA_STOCKS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "price": 235.50, "change": 2.45, "changePercent": 1.05},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "price": 420.75, "change": 3.20, "changePercent": 0.77},
    {"symbol": "NVDA", "name": "NVIDIA Corp.", "price": 875.30, "change": 12.50, "changePercent": 1.45},
    {"symbol": "TSLA", "name": "Tesla Inc.", "price": 248.90, "change": 5.10, "changePercent": 2.09},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "price": 180.45, "change": 2.15, "changePercent": 1.21},
    {"symbol": "META", "name": "Meta Platforms", "price": 595.23, "change": 8.75, "changePercent": 1.49},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "price": 195.30, "change": 4.20, "changePercent": 2.20},
    {"symbol": "JPM", "name": "JPMorgan Chase", "price": 225.10, "change": 1.85, "changePercent": 0.83},
    {"symbol": "V", "name": "Visa Inc.", "price": 305.75, "change": 3.45, "changePercent": 1.14},
    {"symbol": "WMT", "name": "Walmart Inc.", "price": 92.50, "change": 0.95, "changePercent": 1.04},
]

MOCK_MILAN_STOCKS = [
    {"symbol": "ISP.MI", "name": "Intesa Sanpaolo", "price": 3.85, "change": 0.12, "changePercent": 3.22},
    {"symbol": "ENI.MI", "name": "ENI S.p.A.", "price": 14.20, "change": 0.35, "changePercent": 2.52},
    {"symbol": "EOAN.MI", "name": "Enel", "price": 6.45, "change": 0.18, "changePercent": 2.87},
    {"symbol": "UCG.MI", "name": "UniCredit", "price": 38.90, "change": 0.85, "changePercent": 2.23},
    {"symbol": "TIT.MI", "name": "Telecom Italia", "price": 0.25, "change": 0.02, "changePercent": 8.00},
    {"symbol": "STM.MI", "name": "STMicroelectronics", "price": 32.10, "change": 0.95, "changePercent": 3.05},
    {"symbol": "FCA.MI", "name": "Ferrari", "price": 285.50, "change": 8.20, "changePercent": 2.95},
    {"symbol": "BPE.MI", "name": "Banco BPM", "price": 5.75, "change": 0.12, "changePercent": 2.13},
    {"symbol": "BMPS.MI", "name": "Banca MPS", "price": 3.95, "change": 0.08, "changePercent": 2.07},
    {"symbol": "PRY.MI", "name": "Prysmian Group", "price": 45.20, "change": 1.15, "changePercent": 2.61},
]

MOCK_SWITZERLAND_STOCKS = [
    {"symbol": "NOVN.SW", "name": "Novartis AG", "price": 98.45, "change": 2.35, "changePercent": 2.44},
    {"symbol": "RHHBY", "name": "Roche Holding AG", "price": 275.30, "change": 5.80, "changePercent": 2.15},
    {"symbol": "ASML", "name": "ASML Holding NV", "price": 645.20, "change": 12.40, "changePercent": 1.96},
    {"symbol": "NESN.SW", "name": "Nestle SA", "price": 85.70, "change": 1.45, "changePercent": 1.72},
    {"symbol": "ABBN.SW", "name": "ABB Ltd", "price": 42.15, "change": 0.85, "changePercent": 2.06},
    {"symbol": "UBSG.SW", "name": "UBS Group AG", "price": 29.80, "change": 0.55, "changePercent": 1.88},
    {"symbol": "GEBN.SW", "name": "Geberit AG", "price": 550.00, "change": 9.50, "changePercent": 1.75},
    {"symbol": "SCMN.SW", "name": "Schindler Holding", "price": 285.40, "change": 5.20, "changePercent": 1.86},
    {"symbol": "BALN.SW", "name": "Baloise Group", "price": 175.80, "change": 3.15, "changePercent": 1.82},
    {"symbol": "ZURN.SW", "name": "Zurich Insurance Group", "price": 495.30, "change": 8.40, "changePercent": 1.72},
]


def get_latest_quote(symbol: str) -> dict:
    try:
        t = yf.Ticker(symbol)
        hist = t.history(period="5d")
        if hist.empty:
            raise ValueError(f"No data for symbol {symbol}")
        last = hist.iloc[-1]
        return {
            "symbol": symbol.upper(),
            "date": str(last.name.date()),
            "close": float(last["Close"]),
            "volume": int(last.get("Volume", 0)),
        }
    except Exception as e:
        raise ValueError(f"Failed to fetch quote for {symbol}: {str(e)}")


def simple_moving_average(symbol: str, start: str | None, end: str | None, window: int = 20) -> list:
    try:
        if start and end:
            df = yf.download(symbol, start=start, end=end, progress=False)
        else:
            df = yf.download(symbol, period="3mo", progress=False)

        if df.empty:
            raise ValueError(f"No data for symbol {symbol} in given range")

        df = df.sort_index()
        df["sma"] = df["Close"].rolling(window=window).mean()
        out = []
        for idx, row in df.iterrows():
            if pd.isna(row["sma"]):
                continue
            out.append({"date": str(idx.date()), "sma": float(row["sma"])})

        return out
    except Exception as e:
        raise ValueError(f"Failed to analyze {symbol}: {str(e)}")


def get_market_winners(market: str) -> dict:
    """
    Ritorna i 10 titoli in rialzo di una borsa
    """
    if market == "USA":
        stocks = sorted(MOCK_USA_STOCKS, key=lambda x: x["changePercent"], reverse=True)[:10]
    elif market == "MILAN":
        stocks = sorted(MOCK_MILAN_STOCKS, key=lambda x: x["changePercent"], reverse=True)[:10]
    elif market == "SWITZERLAND":
        stocks = sorted(MOCK_SWITZERLAND_STOCKS, key=lambda x: x["changePercent"], reverse=True)[:10]
    else:
        stocks = []
    
    return {
        "market": market,
        "type": "winners",
        "timestamp": datetime.now().isoformat(),
        "stocks": stocks
    }


def get_market_losers(market: str) -> dict:
    """
    Ritorna i 10 titoli in ribasso di una borsa
    """
    if market == "USA":
        stocks = sorted(MOCK_USA_STOCKS, key=lambda x: x["changePercent"])[:10]
    elif market == "MILAN":
        stocks = sorted(MOCK_MILAN_STOCKS, key=lambda x: x["changePercent"])[:10]
    elif market == "SWITZERLAND":
        stocks = sorted(MOCK_SWITZERLAND_STOCKS, key=lambda x: x["changePercent"])[:10]
    else:
        stocks = []
    
    return {
        "market": market,
        "type": "losers",
        "timestamp": datetime.now().isoformat(),
        "stocks": stocks
    }

