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

def handl_sector(sector):

    params ={'api_key': f'{API_KEY}', 'url': f'https://ticker.finology.in/sector/{sector}'}
    # Make the request using Scraper API
    response = requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.select("tbody tr")
    data=[]
    for r in table:
        td = r.select("td")
        company_name=td[0].get_text().replace("\n","")
        price = td[1].get_text().replace("(","")
        change=td[-1].get_text().replace("\n","")
        data.append({"company_name":company_name,"price":price,"change":change})

    return data