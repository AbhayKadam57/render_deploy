import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
import sys
import html5lib
from dotenv import load_dotenv, find_dotenv
from functions.getstocksymbols_name import *
from functions.Get_historical_data import *
load_dotenv(find_dotenv())

sys.stdout.reconfigure(encoding='utf-8')

API_KEY=os.getenv("API_KEY")

URL=os.getenv("SCRAPE_URL")

def handl_stock_details(stock):

    # e.g-bandhan-bank-limited

    query= get_name_symbols(stock)

    c_name=query['name']

    symbol =query['symbol']

    print(c_name)


    params ={'api_key': f'{API_KEY}', 'url': f'https://upstox.com/stocks/{c_name}-share-price'}

    # Make the request using Scraper API
    response =requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html5lib")

    title =soup.select("title")
    print(title)

    print()

    stock_img= soup.select(".mr-12")[0].find("img")['src'] or ""

    # print(stock_img)

    stock_name = soup.select(".stock-name")[0].text

    # print(stock_name)


    stock_price = soup.select(".current-price.pricing")[0].text

    # print(stock_price)

    stock_price_chg=soup.select(".profit-lose.price-stats")[0].text

    # print(stock_price_chg)

    try:
        stock_recomend = soup.select(".update-btn.button.outline-btn.text-uppercase")[0].text
    except IndexError:
        stock_recomend = ""

    # print(stock_recomend)


    p = soup.select("#company-profile-desc")[0].text.strip()

    table_1= soup.select(".list-unstyled.stock-summary-list")[0]

    list_1 = table_1.select("li")

    stock_summary=[]

    for row in list_1:

        content = row.select("div")
        data={content[0].text:content[1].get_text()}
        stock_summary.append(data)
    
    # print(stock_summry)

    table_2 = soup.select(".list-unstyled.stock-summary-list")[1]


    if table_2 is not None:

        list_2 = table_2.select("li") or[]

        stock_key_indices=[]

        for row in list_2:

            content = row.select("div")
            data={content[0].text:content[1].get_text()}
            stock_key_indices.append(data)

    # print(stock_key_indices)

    table_3 = soup.select(".stock-summary-wrap.profitability-content")[1]

    list_3 = table_3.select("li")



    stock_profitablity_ratio=[]

    for row in list_3:

        content = row.select("div")
        data={content[0].select("div")[0].text:content[0].select("div")[1].text}
        stock_profitablity_ratio.append(data)

    # print(stock_profitablity_ratio)


    table_4 = soup.select(".stock-summary-wrap.profitability-content")[1]

    list_4 = table_4.select("li")

    stock_operational_ratio=[]

    for row in list_4:

        content = row.select("div")
        data={content[0].select("div")[0].text:content[0].select("div")[1].text}
        stock_operational_ratio.append(data)

    # print(stock_operational_ratio)

    table_5 = soup.select(".stock-summary-wrap.profitability-content")[-1]

    list_5 = table_5.select("li")

    stock_valuation_ratio=[]

    for row in list_5:

        content = row.select("div")
        data={content[0].select("div")[0].text:content[0].select("div")[1].text}
        stock_valuation_ratio.append(data)

    # print(stock_operational_ratio)


    table_5= soup.select(".list-unstyled.w-100.shareholding-graph")[0]

    list_5 = table_5.select("li")


    stock_holding=[]

    for row in list_5:
        content=row.select("div")
        data={content[1].get_text():content[2].get_text()}
        stock_holding.append(data)

    # print(stock_holding)

    # historical_data=get_historical_data(symbol)

    results =[{'stock_name':stock_name,'symbol':symbol,"stock_profile":p,"stock_img":stock_img,"stock_price":stock_price,"stock_price_chg":stock_price_chg,'stock_recomend':stock_recomend,"stock_summary":stock_summary,"stock_key_indices":stock_key_indices,"stock_profitablity_ratio":stock_profitablity_ratio,"stock_operation_ratio":stock_operational_ratio,"stock_valuation_ratio":stock_valuation_ratio,"stock_holding":stock_holding}]


    return results


