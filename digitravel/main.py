from scraper import fetch_page, parse_page, parse_detail_plan
import csv

url= "https://digitravel.store/shop/"

page_content = fetch_page(url)

# print(page_content)


if page_content:
    product_data = parse_page(page_content)
    print("Product Data:", product_data)
    
    for product in product_data:
        product_link = product.get('productlink')
        if product_link:
            product_details = fetch_page(product_link)
            if product_details:
                product_data = parse_detail_plan(product_details)
            print(f"Product Link: {product_link}, Product Details: ")
else:
    print("Gagal mengambil data dari URL.")