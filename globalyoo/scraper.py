import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    headers = {
        "User-Agent": "PostmanRuntime/7.28.4"
    }
    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()

def fetch_all_plan(url):
    headers = {
        "User-Agent": "PostmanRuntime/7.28.4"
    }
    response = requests.get(url, headers=headers)
    if(response.status_code == 200):
        return response.json()
    else: 
        return None