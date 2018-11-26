import requests
import re
from bs4 import BeautifulSoup
from collections import namedtuple
from decimal import Decimal
from dateutil import parser
rss_hostname = "https://www.ecb.europa.eu"
rss_list_url = "https://www.ecb.europa.eu/home/html/rss.en.html"
rss_url_pattern = re.compile(r'(\/rss\/fxref-[\w]+.html)')

ScrapResult = namedtuple('ScrapResult','date base_currency target_currency exchange_rate')
def scrap_rss_urls():
    request = requests.get(rss_list_url)
    request.raise_for_status()
    response = request.text
    matches = re.findall(rss_url_pattern,response)
    urls = [rss_hostname+x for x in matches]
    return urls

def scrap_currency_rss(url):
    request = requests.get(url)
    request.raise_for_status()
    response = request.content
    soup = BeautifulSoup(response, "html.parser")
    items = soup.find_all('item')
    results = []
    for item in items:
        date = parser.parse(item.find('dc:date').text)
        base_currency = item.find('cb:basecurrency').text
        target_currency = item.find('cb:targetcurrency').text
        exchange_rate =  Decimal(item.find('cb:value').text)
        results.append(ScrapResult(date,base_currency,target_currency,exchange_rate))
    return results