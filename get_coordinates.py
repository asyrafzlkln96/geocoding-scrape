import googlemaps

def get_lat_long(api_key, address):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(address)

    if geocode_result and len(geocode_result) > 0:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None