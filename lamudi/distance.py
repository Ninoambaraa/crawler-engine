import math

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

# Example usage
coord_origin = (-8.6501085, 115.2215519) 
coord_target = (-8.452517, 115.138735)   

distance = haversine_distance(coord_origin, coord_target)
print(distance)
print(f"The distance between the origin and the target is {distance:.2f} kilometers.")