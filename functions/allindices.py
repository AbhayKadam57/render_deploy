import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY=os.getenv("API_KEY")

URL=os.getenv("SCRAPE_URL")


def handl_all_indices():

    params ={'api_key': f'{API_KEY}', 'url': 'https://groww.in/indices'}

    # Make the request using Scraper API
    response = requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')

    soup = BeautifulSoup(response.content, "html.parser")

    rows = soup.select("tbody tr")
    data=[]
    for r in rows:
        td = r.select("td")
        company = td[0].get_text()
        last_trade =td[1].get_text()
        day_chg = td[2].get_text()
        high=td[3].get_text()
        low=td[4].get_text()
        open=td[5].get_text()
        prev_close=td[6].get_text()
        data.append({'company': company, 'last_trade': last_trade, 'day_chg': day_chg, 'high': high, 'low': low,'open':open,'prev_close':prev_close})

    json_data=(data)
    
    return json_data