import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Plot df data for each ticker


def plot_df(df, ticker):

    # Plot df data (Adj Close) for each ticker
        df[[ticker]].plot(title=f"Adj Close Prices for {ticker}", figsize=(12, 6))
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.legend([ticker])
        plt.show()


def plot_ohlc_matplotlib(ohlc_df, ticker):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Extract OHLC data
    dates = ohlc_df.index
    opens = ohlc_df[ticker + "_Open"]
    highs = ohlc_df[ticker + "_High"]
    lows = ohlc_df[ticker + "_Low"]
    closes = ohlc_df[ticker + "_Close"]

    # Plot candlestick chart with coloring based on gain or loss
    for i in range(len(dates)):
        if closes.iloc[i] > opens.iloc[i]:
            color = 'green'
        elif closes.iloc[i] < opens.iloc[i]:
            color = 'red'
        else:
            color = 'black'

        ax.plot([mdates.date2num(dates[i]), mdates.date2num(dates[i])], [lows.iloc[i], highs.iloc[i]], color=color, linewidth=1)
        ax.plot([mdates.date2num(dates[i]), mdates.date2num(dates[i])], [opens.iloc[i], closes.iloc[i]], color=color, linewidth=4)

    # Formatting the chart
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.set_title(f"Candlestick Chart for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)

    plt.show()
