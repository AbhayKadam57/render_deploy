import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
import sys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

sys.stdout.reconfigure(encoding='utf-8')

API_KEY=os.getenv("API_KEY")

URL=os.getenv("SCRAPE_URL")

#categotylist =["intraday-stocks-most-traded","sip-popular-stocks","dividend-stocks","penny-stocks","high-return-stocks","multibagger-stocks"]


def handl_stock_collection(cat):
    params ={'api_key': f'{API_KEY}', 'url': f'https://www.indmoney.com/stocks/category/{cat}'}

    # Make the request using Scraper API
    response = requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table container
    table_container = soup.find('div', class_='flex flex-col w-3/4 flex-1')

    # Find all table rows
    rows = table_container.find_all('a', class_='border-b py-3 lg:pl-3 flex flex-col')

    # Iterate over the rows and extract the data

    data=[]
    for row in rows[1:]:

        name = row.select(".font-normal")[0].get_text()
        price = row.select(".text-brand-black.text-sm")[1].get_text()
        per_chg= row.select(".pl-1")[0].get_text()
        volume= row.select(".text-brand-black.text-sm")[2].get_text()

        if cat=="dividend-stocks":
            dividende_yeild= row.select(".text-brand-black.text-sm")[-1].get_text()
            data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"dividende_yeild":dividende_yeild}) 
        if cat=="high-return-stocks" or cat=="multibagger-stocks":
            three_yr_ret= row.select(".text-brand-black.text-sm")[-1].get_text()
            data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"three_yr_ret":three_yr_ret})
        else:
            market_cap= row.select(".text-brand-black.text-sm")[-1].get_text()
            data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"market_cap":market_cap}) 
    return data

