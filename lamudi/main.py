import requests
from bs4 import BeautifulSoup
import math
import csv

def extract_data(soup):
    listings = soup.find_all("div", class_="ListingCell-AllInfo ListingUnit")
    data = []

    for listing in listings:
        listing_data = {}
        
        # Extract basic listing details
        title_tag = listing.find("h3", class_="ListingCell-KeyInfo-title")
        title = title_tag.text.strip() if title_tag else None
        
        price_tag = listing.find("span", class_="PriceSection-FirstPrice")
        price = price_tag.text.strip() if price_tag else None
        
        address_tag = listing.find("span", class_="ListingCell-KeyInfo-address-text")
        address = address_tag.text.strip() if address_tag else None
        
        img_tag = listing.find("img")
        image_url = img_tag['src'] if img_tag else None
        
        url_tag = listing.find("a", class_="js-listing-link")
        url = url_tag['href'] if url_tag else None
        
        # Extract additional attributes from data attributes
        data_car_spaces = listing.get('data-car_spaces', None)
        data_bedrooms = listing.get('data-bedrooms', None)
        data_bathrooms = listing.get('data-bathrooms', None)
        data_furnished = listing.get('data-furnished', None)
        data_building_size = listing.get('data-building_size', None)
        data_land_size = listing.get('data-land_size', None)
        data_sku = listing.get('data-sku', None)
        data_geo_point = listing.get('data-geo-point', None)
        data_category = listing.get('data-category', None)
        
        # Parse geo-point if available
        if data_geo_point and data_geo_point.lower() != 'null':
            try:
                # Remove brackets and split the string
                coords = data_geo_point.strip('[]').split(',')
                latitude = float(coords[1])
                longitude = float(coords[0])
                geo_coords = (latitude, longitude)
            except (ValueError, IndexError):
                geo_coords = None
        else:
            geo_coords = None
        
        listing_data['title'] = title
        listing_data['price'] = price
        listing_data['address'] = address
        listing_data['image_url'] = image_url
        listing_data['url'] = url
        listing_data['data_category'] = data_category
        listing_data['data_car_spaces'] = data_car_spaces
        listing_data['data_bedrooms'] = data_bedrooms
        listing_data['data_bathrooms'] = data_bathrooms
        listing_data['data_furnished'] = data_furnished
        listing_data['data_building_size'] = data_building_size
        listing_data['data_land_size'] = data_land_size
        listing_data['data_sku'] = data_sku
        listing_data['data_geo_point'] = geo_coords
        
        data.append(listing_data)
    
    return data

def haversine_distance(coord1, coord2):
    """
    Calculate the great-circle distance between two points
    on the Earth's surface specified in decimal degrees using the Haversine formula.
    
    Parameters:
    coord1 : tuple
        A tuple representing the latitude and longitude of the first point (lat1, lon1).
    coord2 : tuple
        A tuple representing the latitude and longitude of the second point (lat2, lon2).
    
    Returns:
    float
        The distance between the two points in kilometers.
    """
    
    # Unpack the coordinates
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of the Earth in kilometers (mean radius)
    r = 6371.01
    
    # Calculate the distance
    distance = r * c
    
    return distance

def scrape_lamudi(base_url, target_coords, pages=50):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    all_data = []
    
    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data = extract_data(soup)
            
            # Calculate distance for each listing and filter those within 1 km
            for item in data:
                geo_coords = item.get('data_geo_point')
                if geo_coords:
                    distance = haversine_distance(target_coords, geo_coords)
                    if distance <= 1.0:  # Distance within 1 km
                        item['distance_from_target'] = round(distance, 2)
                        all_data.append(item)
                else:
                    item['distance_from_target'] = None
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            break  # Stop if a page fails to load
    
    return all_data

def save_to_csv(data, filename):
    if not data:
        print("No data to write to CSV.")
        return
    
    # Define CSV column headers based on keys in the first dictionary
    headers = data[0].keys()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data successfully saved to {filename}")

# Example usage
target_coords = (-8.6501085, 115.2215519)  # Coordinates of the target location
base_url = 'https://www.lamudi.co.id/jual/bali'
data = scrape_lamudi(base_url, target_coords, pages=50)

# Save data to CSV
save_to_csv(data, 'bali.csv')
