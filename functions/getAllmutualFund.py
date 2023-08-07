import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import re
import sys
import aiohttp
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

sys.stdout.reconfigure(encoding="utf-8")

API_KEY = os.getenv("API_KEY")

URL = os.getenv("SCRAPE_URL")


async def fetch_html(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.text()


async def handl_all_MutualFund_data(mutualfund, code):
    params = {
        "api_key": f"{API_KEY}",
        "url": f"https://groww.in/mutual-funds/{mutualfund}",
    }

    # Make the request using Scraper API
    response = requests.get(f"https://groww.in/mutual-funds/{mutualfund}")
    # response_content = await fetch_html(URL, params)
    # response = requests.get('https://groww.in/indices')

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select("title")

    scheme_name = soup.find("h1", class_="mfh239SchemeName display24").get_text()
    # scheme_name_1 = soup.find("h1", class_="mfh239SchemeName display24").get_text()
    # print(scheme_name_1)

    # scheme_name = "Abhay"

    day_chg = soup.find(class_="mfh239OneDay").get_text()

    nav_today = soup.select(".tb10Table.fd12Table")

    # this give rating and fund size, minimum sip
    rows = nav_today[0].find_all("tr")
    rows1 = nav_today[1].find_all("tr")

    data = []

    for r in rows:
        td = r.select("td")

        obj = {td[0].get_text(): td[1].get_text()}
        data.append(obj)

    for r in rows1:
        td = r.select("td")

        obj = {td[0].get_text(): td[1].get_text()}
        data.append(obj)

    holdingTableRow = soup.select(".holdings101Row")

    HoldingTable = []

    for r in holdingTableRow:
        td = r.select("td")
        name = td[0].get_text()
        sector = td[1].get_text()
        instrument = td[2].get_text()
        assests = td[3].get_text()
        HoldingTable.append(
            {
                "name": name,
                "sector": sector,
                "instrument": instrument,
                "assests": assests,
            }
        )

    returnData = []

    Returns = soup.select(".tb10Td")

    one_year_return = Returns[0].get_text()

    three_year_return = Returns[1].get_text()

    five_year_return = Returns[2].get_text()

    All_return = Returns[3].get_text()

    returnData.append({"one_year_return": one_year_return})
    returnData.append({"three_year_return": three_year_return})
    returnData.append({"five_year_return": five_year_return})
    returnData.append({"All_return": All_return})

    ratioData = []

    expenseRation = soup.select(".mf320Heading")

    Expenseration = expenseRation[3].get_text()
    ExitLoad = expenseRation[4].get_text()
    StampDuty = expenseRation[5].get_text()
    Tax = expenseRation[6].get_text()

    ratioData.append({"ExpenseRation": Expenseration})
    ratioData.append({"ExitLoad": ExitLoad})
    ratioData.append({"StampDuty": StampDuty})
    ratioData.append({"Tax": Tax})

    fundManagers = soup.select(".fm982PersonName.fs16.fw500.clrText130")

    fundManagerData = []

    for r in fundManagers:
        fundManagerData.append(r.get_text())

    finalResult = [
        {
            "scheme_name": scheme_name,
            "day_chg": day_chg,
            "fundamentals": data,
            "Holdings": HoldingTable,
            "returns": returnData,
            "ratio": ratioData,
            "fundmanagers": fundManagerData,
            "link": mutualfund,
            "code": code,
        }
    ]

    return finalResult
