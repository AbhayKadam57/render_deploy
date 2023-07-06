from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions.allindices import *
from functions.topstocks import *
from functions.sectorwisestocks import *
from functions.yearhighlow import *
from functions.stocksbymovingavg import *
from functions.themebasecollection import *
from functions.stockcollection import *
from functions.stockdetails import *
from functions.getonefayhistory import *
from functions.getTopGainers import *
from functions.getStockDetails import *


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_welcome():
    return{"status":200,"message":"Welcome to Stock api"}

@app.get("/allindices")
def read_root():
    list = handl_all_indices()
    return list

@app.get("/topstocks/{cat}")
def read_top_stocks(cat,skip:int=0,limit:int=10):
    list= handl_top_stocks(cat)
    return list[skip:skip+limit]

@app.get("/sector-wise-data/{sector}")
def read_sector_wise_data(sector):
    list = handl_sector(sector)
    return list

@app.get("/fifty-two-week-data/{status}")
def read_fifty_two_week_data(status):
    list=handl_year_high(status)
    return list

@app.get("/stock-by-rsi-dma/{cat}")
def read_stocks_rsi_dma(cat):
    list=handl_dma_rsi(cat)
    return list


#get all it,pharma etc stock
@app.get("/theme-based-stocks/{cat}")
def read_theme_based_stocks(cat):
    list=handl_themebase_stocks(cat)
    return list

@app.get("/stockcollection/{cat}")
def read_stock_collection(cat):
    list=handl_stock_collection(cat)
    return list


@app.get("/stock-details/{stock}/{stock_code}")
def read_stock_details(stock,stock_code):
    list=handl_stock_details(stock,stock_code)
    return list



#get all gainers, losers , 52 week high low
@app.get("/all-top-stocks/{cat}")
def read_all_top_stocks(cat):
    list=hadle_top_rated(cat)
    return list


@app.get("/one-day-hist/{stock_symbol}")
def read_one_day_hist(stock_symbol):
    list = hadle_one_day_history(stock_symbol)
    return list

@app.get("/one-week-hist/{stock_symbol}")
def read_one_week_hist(stock_symbol):
    list = hanle_one_week(stock_symbol)
    return list

@app.get("/one-month-hist/{stock_symbol}")
def read_one_month_hist(stock_symbol):
    list = hanle_one_month(stock_symbol)
    return list

@app.get("/one-year-hist/{stock_symbol}")
def read_one_year_hist(stock_symbol):
    list = handl_one_year(stock_symbol)
    return list

@app.get("/three-year-hist/{stock_symbol}")
def read_three_year_hist(stock_symbol):
    list = handl_three_year(stock_symbol)
    return list

@app.get("/five-year-hist/{stock_symbol}")
def read_five_year_hist(stock_symbol):
    list = handl_five_years(stock_symbol)
    return list

@app.get("/stock-details-all/{name}")
def read_stock_all_details(name):
    list = get_stock_details(name)
    return list