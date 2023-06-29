import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re


def handl_all_indices():

    URL = "https://groww.in/indices"


    params ={'api_key': '568da9e6d253489d078b9d29c83dfe54', 'url': 'https://groww.in/indices'}

    # Make the request using Scraper API
    response = requests.get('http://api.scraperapi.com/', params=urlencode(params))

    soup = BeautifulSoup(response.content, "html5lib")

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
