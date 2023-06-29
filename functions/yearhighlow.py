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


def handl_year_high(status):

    params ={'api_key': f'{API_KEY}', 'url': f'https://ticker.finology.in/market/{status}'}
    # Make the request using Scraper API
    response = requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html.parser")

    rows = soup.select("tr")[1:]
    data=[]
    for r in rows:
        td =r.select("td")
        company_name= td[1].get_text()
        price=td[2].get_text()
        day_high_or_low=td[-1].get_text()
        data.append({"company_name":company_name,"price":price,"day_high_or_low":day_high_or_low})

    return data