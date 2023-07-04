import yfinance as yf
from datetime import datetime, timedelta

def hadle_one_day_history(stock_symbol):

    symbol = stock_symbol+".NS"

    one_day_hist = yf.download(symbol,period="1d",interval="1m")

    data = one_day_hist.to_dict()

    return data["Close"]


def hanle_one_week(stock_symbol):
    symbol = stock_symbol+".NS"
    date_format = "%Y-%m-%d"
    current_date = datetime.now()+timedelta(days=1)
    current_date_formatted = current_date.strftime(date_format)
    print(current_date_formatted)

    one_week_ago = current_date - timedelta(weeks=1)
    print(one_week_ago)
    one_week_ago_formatted = one_week_ago.strftime(date_format)
    data_one_week = yf.download(symbol, start=one_week_ago_formatted, end=current_date_formatted,interval="5m")
    one_week_history =data_one_week.to_dict()

    return one_week_history["Close"]

def hanle_one_month(stock_symbol):
    symbol = stock_symbol+".NS"
    date_format = "%Y-%m-%d"
    current_date = datetime.now()+timedelta(days=1)
    current_date_formatted = current_date.strftime(date_format)
    

    one_month_ago = current_date - timedelta(days=30)
    one_month_ago_formatted = one_month_ago.strftime(date_format)
    data_month = yf.download(symbol, start=one_month_ago_formatted, end=current_date_formatted,interval="30m")
    one_month_history =data_month.to_dict()
    return one_month_history["Close"]


def handl_one_year(stock_symbol):
    symbol = stock_symbol+".NS"
    date_format = "%Y-%m-%d"
    current_date = datetime.now()+timedelta(days=1)
    current_date_formatted = current_date.strftime(date_format)


    one_year_ago = current_date - timedelta(days=365)
    one_year_ago_formatted = one_year_ago.strftime(date_format)
    data_year = yf.download(symbol, start=one_year_ago_formatted, end=current_date_formatted,interval="1d")
    one_year_history =data_year.to_dict()
    
    return one_year_history["Close"]

def handl_three_year(stock_symbol):
    symbol = stock_symbol+".NS"
    date_format = "%Y-%m-%d"
    current_date = datetime.now()+timedelta(days=1)
    current_date_formatted = current_date.strftime(date_format)
    

    three_years_ago = current_date - timedelta(days=3*365)

    three_years_ago_formatted = three_years_ago.strftime(date_format)
    data_three_year = yf.download(symbol, start=three_years_ago_formatted, end=current_date_formatted,interval="5d")
    three_years_history =data_three_year.to_dict()

    return three_years_history["Close"]

def handl_five_years(stock_symbol):
    symbol = stock_symbol+".NS"
    date_format = "%Y-%m-%d"
    current_date = datetime.now()+timedelta(days=1)
    current_date_formatted = current_date.strftime(date_format)
    

    five_years_ago = current_date - timedelta(days=5*365)

    five_years_ago_formatted = five_years_ago.strftime(date_format)

    data_five_year = yf.download(symbol, start=five_years_ago_formatted, end=current_date_formatted,interval="1wk")

    five_years_history =data_five_year.to_dict()

    return five_years_history["Close"]