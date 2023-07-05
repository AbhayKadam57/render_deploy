import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
import sys
import html5lib
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

sys.stdout.reconfigure(encoding='utf-8')

API_KEY=os.getenv("API_KEY")

URL=os.getenv("SCRAPE_URL")


#this is for to get 52-week high,low,top gainers losers

def hadle_top_rated(cat):

    params ={'api_key': f'{API_KEY}', 'url': f'https://groww.in/markets/{cat}?index=GIDXNIFTY100'}

    # Make the request using Scraper API
    response =requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html5lib")

    title =soup.select("title")

    rows = soup.select("tbody tr")

    data=[]

    for row in rows:

        link= row.select("a")[0]["href"].split("/")[-1]+"-share-price"
        print(link)
        td=row.select("td")
        company_name=td[0].get_text()
        price=td[2].get_text()
        pattern = r"₹([\d,]+\.\d{2})"
        matches = re.search(pattern, price)

        if matches:
            market_price=matches.group(0)


        fifty_week_high=td[3].get_text()
        fifty_week_low=td[3].get_text()
        data.append({"company_name":company_name,"short_name":link,"market_price":market_price,"fifty_week_high":fifty_week_high,"fifty_week_low":fifty_week_low})

    return data

hadle_top_rated("top-gainers")