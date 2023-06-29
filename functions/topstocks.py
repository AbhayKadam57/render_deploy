import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
from dotenv import load_dotenv, find_dotenv
import sys
import time

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")
URL = os.getenv("SCRAPE_URL")



def handl_top_stocks(cat,index):

    params = {'api_key': API_KEY, 'url': f'https://groww.in/markets/{cat}?index={index}'}
    response = requests.get(URL, params=(params))
    soup = BeautifulSoup(response.content, "html.parser")

    company_rows = soup.select(".fs14.mtp438RowDiv")

    data=[]

    for row in company_rows:
        text = row.get_text().replace("₹", "/")
        reframe = text.replace("b'", "")
        array = reframe.split("/")
        company_name = array[0]
        market_price = array[1]
        f_w_low = array[2]
        f_w_high = array[3]
        data.append({
            "company_name": company_name,
            "market_price": market_price,
            "f_w_low": f_w_low,
            "f_w_high": f_w_high
        })

    return data

handl_top_stocks("top-gainers","GIDXNIFMDCP100")