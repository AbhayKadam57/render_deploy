# import yfinance as yf
# import json
# from functions.getstocksymbols_name import *


# def get_stock_details(name):
#     data = get_name_symbols(name)

#     symbol = data["symbol"]

#     irctc = yf.Ticker(f"{symbol}.NS")

#     print("from getdetails", irctc)

#     info = irctc.get_info()

#     print("info=====17", info)

#     finace_info = irctc.get_financials().to_json()

#     basic_info = info

#     finance_ratio = json.loads(finace_info)

#     return {"basic_info": basic_info, "finance_ratio": finance_ratio}
import yfinance as yf
import json
from functions.getstocksymbols_name import (
    get_name_symbols,
)  # Import the correct function


def get_stock_details(stock_name):
    data = get_name_symbols(stock_name)

    if "symbol" not in data:
        return {"error": "Symbol not found for the given stock name"}

    symbol = data["symbol"]
    stock_exchange = "NS"

    print(f"{symbol}.{stock_exchange}")

    stock_ticker = f"{symbol}.{stock_exchange}"
    stock = yf.Ticker(stock_ticker)

    # print("Stock details for", stock_ticker)

    info = stock.get_info()

    # print("Basic Info:", info)

    financials = stock.get_financials().to_json()

    finance_ratio = json.loads(financials)

    return {"basic_info": info, "finance_ratio": finance_ratio}
