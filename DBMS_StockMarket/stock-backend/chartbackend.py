import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_trend(symbol, period='1mo', interval='1d'):
    # Fetch stock data
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period, interval=interval)

    if hist.empty:
        print(f"No data found for {symbol}")
        return

    # Plot Price Trend
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(hist.index, hist['Close'], label='Close Price', color='blue', linewidth=2)
    ax1.set_ylabel('Price (INR)', color='blue')
    ax1.set_title(f"{symbol} - Stock Price & Volume")
    ax1.tick_params(axis='y', labelcolor='blue')

    # Plot Volume on secondary axis
    ax2 = ax1.twinx()
    ax2.bar(hist.index, hist['Volume'], color='lightgray', alpha=0.6, label='Volume')
    ax2.set_ylabel('Volume', color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    # Show plot
    fig.tight_layout()
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()

# Example usage:
stock_symbols = [
    "BAJFINANCE.NS",     # Bajaj Finance
    "VEDL.NS",           # Vedanta
    "JINDALSTEL.NS",     # Jindal Steel and Power
    "AUROPHARMA.NS",     # Aurobindo Pharma
    "ADANIENT.NS",       # Adani Enterprises
    "HINDUNILVR.NS",     # Hindustan Unilever
    "RELIANCE.NS",       # Reliance Industries
    "M&M.NS",            # Mahindra & Mahindra
    "ITC.NS",            # ITC Ltd
    "TATACONSUM.NS",     # Tata Consumers
    "HDFCBANK.NS",       # HDFC Bank
    "BHARTIARTL.NS",     # Bharti Airtel
    "INFY.NS",           # Infosys
    "LT.NS",             # Larsen & Toubro
    "SUNPHARMA.NS",      # Sun Pharma
    "HCLTECH.NS",        # HCL Technologies
    "NTPC.NS"            # NTPC
]

# Loop through and plot each stock trend
for symbol in stock_symbols:
    plot_stock_trend(symbol)
