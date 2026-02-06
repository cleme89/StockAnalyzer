import pandas as pd
import yfinance as yf


def get_latest_quote(symbol: str) -> dict:
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


def simple_moving_average(symbol: str, start: str | None, end: str | None, window: int = 20) -> list:
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
