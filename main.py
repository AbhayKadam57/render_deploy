from fastapi import FastAPI
from functions.allindices import *
from functions.topstocks import *
from functions.sectorwisestocks import *
from functions.yearhighlow import *
from functions.stocksbymovingavg import *
from functions.themebasecollection import *
from functions.stockcollection import *
from functions.stockdetails import *

app = FastAPI()

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

@app.get("/theme-based-stocks/{cat}")
def read_theme_based_stocks(cat):
    list=handl_themebase_stocks(cat)
    return list

@app.get("/stockcollection/{cat}")
def read_stock_collection(cat):
    list=handl_stock_collection(cat)
    return list


@app.get("/stock-details/{stock}")
def read_stock_details(stock):
    list=handl_stock_details(stock)
    return list