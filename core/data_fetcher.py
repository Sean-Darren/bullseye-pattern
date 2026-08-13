import yfinance as yf
import pandas as pd

class MarketDataFetcher:
    @staticmethod
    def fetch_ohlc(ticker: str, period: str = "6mo", interval: str = "1d") -> pd.DataFrame:
        "fetch open high low close volume data using yfinance"

        ticker_clean = ticker.strip().upper()

        try:
            data = yf.download(ticker_clean, period=period, interval=interval, progress=False)

        except Exception as exc:
            raise ValueError(f"failed to fetch {ticker_clean}: {exc}") from exc

        if data.empty:
            raise ValueError(f"No Market data returned for {ticker_clean}")

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        return data