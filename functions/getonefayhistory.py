import yfinance as yf


def hadle_one_day_history(stock_symbol):

    symbol = stock_symbol+".NS"

    one_day_hist = yf.download(symbol,period="1d",interval="1m")

    data = one_day_hist.to_dict()

    return data["Close"]