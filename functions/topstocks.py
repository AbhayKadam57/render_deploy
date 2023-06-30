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



def handl_top_stocks(cat):

    params = {'api_key': API_KEY, 'url': f'https://ticker.finology.in/market/{cat}'}
    response = requests.get(URL, params=(params))
    soup = BeautifulSoup(response.content, "html.parser")

    company_rows = soup.select("tbody tr")
    data=[]
    for r in company_rows:
        td = r.select("td")

        company_name= td[1].get_text()
        market_price=td[2].get_text()
        per_chg=td[3].get_text()    

        data.append({'company_name':company_name,'market_price':market_price,'per_chg':per_chg})

    return data
    

