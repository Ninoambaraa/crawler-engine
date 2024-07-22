import requests
import csv
import os
from bs4 import BeautifulSoup
import json


url="https://digitravel.store/esim-instan/"


def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url)
    if(response.status_code == 200):
        return response.text
    else:
        return None
    
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_data = []
    
    spans = soup.find_all('span', class_='gtm4wp_productdata')
    for span in spans:
        data = span.get('data-gtm4wp_product_data')
        if data:
            product_data.append(json.loads(data))
    
    return product_data

def parse_detail_plan(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_data = []
    return product_data
