from datetime import datetime, timedelta
import yfinance as yf


def get_historical_data(symbol):
    # Current date
    current_date = datetime.now()

    # 1 day ago
    one_day_ago = current_date - timedelta(days=1)

    # 1 week ago
    one_week_ago = current_date - timedelta(weeks=1)

    # 1 month ago (approximation)
    one_month_ago = current_date - timedelta(days=30)

    # 1 year ago (approximation)
    one_year_ago = current_date - timedelta(days=365)

    # 3 years ago (approximation)
    three_years_ago = current_date - timedelta(days=3*365)

    # 5 years ago (approximation)
    five_years_ago = current_date - timedelta(days=5*365)

    # Formatting the dates
    date_format = "%Y-%m-%d"
    current_date_formatted = current_date.strftime(date_format)
    one_day_ago_formatted = one_day_ago.strftime(date_format)
    one_week_ago_formatted = one_week_ago.strftime(date_format)
    one_month_ago_formatted = one_month_ago.strftime(date_format)
    one_year_ago_formatted = one_year_ago.strftime(date_format)
    three_years_ago_formatted = three_years_ago.strftime(date_format)
    five_years_ago_formatted = five_years_ago.strftime(date_format)

    # Define the stock symbol or ticker
    stock_symbol = symbol+".NS"  # Example: Apple Inc. (AAPL)

    # Fetch historical data
    data_one_day = yf.download(stock_symbol, start=one_day_ago_formatted, end=current_date_formatted,interval="1m")
    data_one_week = yf.download(stock_symbol, start=one_week_ago_formatted, end=current_date_formatted,interval="5m")
    data_month = yf.download(stock_symbol, start=one_month_ago_formatted, end=current_date_formatted,interval="30m")
    data_year = yf.download(stock_symbol, start=one_year_ago_formatted, end=current_date_formatted,interval="1d")
    data_three_year = yf.download(stock_symbol, start=three_years_ago_formatted, end=current_date_formatted,interval="5d")
    data_five_year = yf.download(stock_symbol, start=five_years_ago_formatted, end=current_date_formatted,interval="1wk")

    # Convert DataFrame to dictionary
    one_day_history =data_one_day.to_dict() or {}
    one_week_history =data_one_week.to_dict()
    one_month_history =data_month.to_dict()
    one_year_history =data_year.to_dict()
    three_years_history =data_three_year.to_dict()
    five_years_history =data_five_year.to_dict()

    # Print the historical data as a dictionary
    return {

        "1day":one_day_history["Close"],
        "1week":one_week_history["Close"],
        "1month":one_month_history["Close"],
        "1year":one_year_history["Close"],
        "3year":three_years_history["Close"],
        "5year":five_years_history["Close"]
    }
