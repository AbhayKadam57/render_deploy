from fastapi import FastAPI
from functions.allindices import *
from functions.topstocks import *
from functions.sectorwisestocks import *
from functions.yearhighlow import *

app = FastAPI()

@app.get("/allindices")
def read_root():
    list = handl_all_indices()
    return list

@app.get("/topstocks/{cat}/{index}")
def read_top_stocks(cat, index):
    list= handl_top_stocks(cat,index)
    return list

@app.get("/sector-wise-data/{sector}")
def read_sector_wise_data(sector):
    list = handl_sector(sector)
    return list

@app.get("/fifty-two-week-data/{status}")
def read_fifty_two_week_data(status):
    list=handl_year_high(status)
    return list