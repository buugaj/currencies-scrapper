import requests
import re

rss_hostname = "https://www.ecb.europa.eu"
rss_list_url = "https://www.ecb.europa.eu/home/html/rss.en.html"
rss_url_pattern = re.compile(r'(\/rss\/fxref-[\w]+.html)')

def scrap_rss_urls():
    request = requests.get(rss_list_url)
    request.raise_for_status()
    response = request.text
    matches = re.findall(rss_url_pattern,response)
    urls = [rss_hostname+x for x in matches]
    return urls

scrap_rss_urls()