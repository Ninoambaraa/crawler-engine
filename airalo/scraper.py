import requests
import csv
import os
from bs4 import BeautifulSoup

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url)
    if(response.status_code == 200):
        return response.text
    else: 
        return None

def fetch_countries(url):
    response = requests.get(url)
    if(response.status_code == 200):
        return response.json()
    else:
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all(class_="store-item aloo")
    data = []
    for t in title:
        data.append(t.get_text())
    return data

def get_detail_countries_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(url)
        return response.text
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 
    return None
    
def parse_page_detail_countries(html):
    soup = BeautifulSoup(html, 'html.parser')
    packages = soup.find_all(class_="c--sim_item-row")
    data_list = []
    
    current_package = {'country': None, 'price': None, 'data': None, 'validity': None}
    
    for package in packages:
        country_elem = package.find("p", {"data-testid": "COVERAGE-row"})
        if country_elem:
            current_package['country'] = country_elem.find_next_sibling("p").get_text(strip=True)

        price_elem = package.find("p", {"data-testid": "PRICE-row"})
        if price_elem:
            current_package['price'] = price_elem.find_next_sibling("p").get_text(strip=True)

        data_elem = package.find("p", {"data-testid": "DATA-row"})
        if data_elem:
            current_package['data'] = data_elem.find_next_sibling("p").get_text(strip=True)

        validity_elem = package.find("p", {"data-testid": "VALIDITY-row"})
        if validity_elem:
            current_package['validity'] = validity_elem.find_next_sibling("p").get_text(strip=True)
        
        if all(current_package.values()):
            data_list.append([current_package['country'], current_package['price'], current_package['data'], current_package['validity']])
            current_package = {'country': None, 'price': None, 'data': None, 'validity': None}

    return data_list

def write_to_csv(data, filename):
    header = ['Country', 'Price', 'Data', 'Validity']
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerows(data)

