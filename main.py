import pandas as pd
import yfinance as yf

# 1. Define the ticker symbol for NIFTY 50
ticker = "^NSEI"

# 2. Connect to Yahoo Finance for this ticker
nifty = yf.Ticker(ticker)

# 3. Download the price history for the last 1 day
data = nifty.history(period="1d")

# 4. Check if data came back and print the closing price
if not data.empty:
    latest_price = data['Close'].iloc[-1]
    print(f"NIFTY 50 Current Quote / Closing Price: ₹{latest_price:.2f}")
else:
    print("Failed to fetch NIFTY quote.")