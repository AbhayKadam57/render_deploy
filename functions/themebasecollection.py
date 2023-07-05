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

#categotylist =["it-stocks,it-stocks-under-200","it-stocks-under-500",it-stocks-in-buy,it-stocks-high-return,it-stocks-high-dividend]
#categotylist =["banking-stocks,it-stocks-under-200","banking-stocks-under-500",banking-stocks-in-buy,banking-stocks-high-return,banking-stocks-high-dividend]
#categotylist =["pharma-stocks,it-stocks-under-200","pharma-stocks-under-500",pharma-stocks-in-buy,pharma-stocks-high-return,pharma-stocks-high-dividend]
#categotylist =["healthcare-stocks,it-stocks-under-200","healthcare-stocks-under-500",healthcare-stocks-in-buy,healthcare-stocks-high-return,healthcare-stocks-high-dividend]


def handl_themebase_stocks(cat):
    params ={'api_key': f'{API_KEY}', 'url': f'https://www.indmoney.com/stocks/category/{cat}'}

    # Make the request using Scraper API
    response = requests.get(f'{URL}', params=urlencode(params))
    # response = requests.get('https://groww.in/indices')
    soup = BeautifulSoup(response.content, "html.parser")

    title=soup.select("title")

    print(title)

    # Find the table container
    table_container = soup.find('div', class_='flex flex-col w-3/4 flex-1')



    # Find all table rows
    rows = table_container.find_all('a', class_='border-b py-3 lg:pl-3 flex flex-col')

    # Iterate over the rows and extract the data

    data=[]
    for row in rows[1:]:
        img = row.select('img')[0]["src"]
        link=row["href"].split('/')[-1]
        name = row.select(".font-normal")[0].get_text()
        price = row.select(".text-brand-black.text-sm")[1].get_text()
        per_chg= row.select(".pl-1")[0].get_text()
        volume= row.select(".text-brand-black.text-sm")[2].get_text()

        data.append({"company_name":name,"link":link,"market_price":price,"per_chg":per_chg,"volume":volume,"img":img}) 

        # string = cat
        # pattern = r"-in-buy"
        # matches = re.search(pattern, string)
        # pattern_1=r"-high-return"
        # matches_1 = re.search(pattern_1,string)
        # pattern_2=r"-high-dividend"
        # matches_2= re.search(pattern_2,string)

        # if matches:
        #     analyst_rating= row.select(".text-brand-black.text-sm")[-1].get_text() 
        #     data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"analyst_rating":analyst_rating})   
        # if matches_1:
        #     one_year_ret= row.select(".text-brand-black.text-sm")[-1].get_text() 
        #     data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"one_year_ret":one_year_ret})
        # if matches_2:
        #     dividend_yeild= row.select(".text-brand-black.text-sm")[-1].get_text() 
        #     data.append({"company_name":name,"market_price":price,"per_chg":per_chg,"volume":volume,"dividend_yeild":dividend_yeild})
    
    return data


