import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

URL = "https://groww.in/indices"


params ={'api_key': '568da9e6d253489d078b9d29c83dfe54', 'url': 'https://groww.in/indices'}

# Make the request using Scraper API
response = requests.get('http://api.scraperapi.com/', params=urlencode(params))


page = BeautifulSoup(response.content, "html.parser")

results = page.find("img")
print(results)

