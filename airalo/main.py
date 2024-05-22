from scraper import fetch_page, parse_page, fetch_countries, parse_page_detail_countries, get_detail_countries_page, write_to_csv

url= "https://airalo.com"
countries_url = "https://www.airalo.com/api/v3/countries?sort=asc"

countries_data = fetch_countries(countries_url)

page_content = fetch_page(url)

all_countries = []


with open('regional.txt', 'r') as file:
    all_countries = [line.strip() for line in file]

if countries_data:
    print("Data countres")
    for item in countries_data:
        all_countries.append(item['slug'])


if all_countries:
    all_data = []
    for country in all_countries:
        detail_country_url = "https://www.airalo.com/"+country+"-esim"
        detail_country_page = get_detail_countries_page(detail_country_url)
        data = parse_page_detail_countries(detail_country_page)
        all_data.append(data)

    
        
    for data in all_data:
        write_to_csv(data, "airalo-data-esim.csv")    


