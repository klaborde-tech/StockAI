import yfinance as yf

def download_stock_data(ticker):
    
    stock = yf.Ticker(ticker)
    
    data = stock.history(period="1y")
    
    print(data.head())
    
    return data

