from scraper import fetch_url
import csv


all_countries = fetch_url("https://play.prod.yomobile.xyz/api/v1.0/esim/countries/")

all_regions = fetch_url("https://play.prod.yomobile.xyz/api/v1.0/esim/regions/?is_global=false")

all_global = fetch_url("https://play.prod.yomobile.xyz/api/v1.0/esim/regions/?is_global=true")


all_plan = []

if all_countries:
    for country_id in all_countries:
        data = fetch_url(f"https://play.prod.yomobile.xyz/api/v5.0/esim/countries/{country_id['id']}/products/")
        if data:
            all_plan.append(data)

if all_regions:
    for region in all_regions:
        data = fetch_url(f"https://play.prod.yomobile.xyz/api/v5.0/esim/regions/{region['id']}/products/")
        if data:
            all_plan.append(data)

if all_global:
    for region in all_global:
        data = fetch_url(f"https://play.prod.yomobile.xyz/api/v5.0/esim/regions/{region['id']}/products/")
        if data:
            all_plan.append(data)


with open('globalyoo-esim-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["duration", "data", "name", "provider", "data_in_mb", "price", "is_promo"])

    for plan in all_plan:
        for item in plan:
            writer.writerow([item["duration"], item["data"], item["name"], item["provider"], item["data_in_mb"], item["price"], item["is_promo"]])
