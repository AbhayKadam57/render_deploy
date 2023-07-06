import yfinance as yf
import json
from functions.getstocksymbols_name import *


def get_stock_details(name):

    data= get_name_symbols(name)

    symbol = data["symbol"]

    irctc = yf.Ticker(F"{symbol}.NS")

    info = irctc.get_info()

    finace_info = irctc.get_financials().to_json()

    basic_info=info

    finance_ratio=json.loads(finace_info)

    return {"basic_info":basic_info,"finance_ratio":finance_ratio}

