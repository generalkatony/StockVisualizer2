import pandas as pd
import yfinance as yf

def data_fetchnpro(nyse_stock_tickers,df,ohlc):
    # Fetch historical data for each ticker and append it to the DataFrame
    for ticker in nyse_stock_tickers:
        stock_data = yf.download(ticker, start="2010-01-01", end="2023-08-17")  # Adjust the end date as needed
        if not stock_data.empty:  # Check if data is available for the specified period
            df[ticker] = stock_data["Adj Close"]
            df[ticker] = stock_data["Adj Close"]
            ohlc[ticker + "_Open"] = stock_data["Open"]
            ohlc[ticker + "_High"] = stock_data["High"]
            ohlc[ticker + "_Low"] = stock_data["Low"]
            ohlc[ticker + "_Close"] = stock_data["Close"]

    # Print the DataFrame
    print(df)
    print(ohlc)

    return df, ohlc