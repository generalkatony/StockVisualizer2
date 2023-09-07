from Plotting import *
from Data_Processing import *

# List of NYSE stock tickers
nyse_stock_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "XPEV"]

# Create an empty DataFrame
df = pd.DataFrame()
ohlc = pd.DataFrame()

# Fetch the data from Yahoo Finance & process into pandas dataframe
data_fetchnpro(nyse_stock_tickers,df,ohlc)

# Call the function to plot each ticker's data
for ticker in nyse_stock_tickers:
    plot_df(df,ticker)

# Call the function to plot the OHLC data for each ticker
for ticker in nyse_stock_tickers:
    plot_ohlc_matplotlib(ohlc, ticker)

