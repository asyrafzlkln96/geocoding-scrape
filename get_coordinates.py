from geopy.geocoders import Nominatim

def get_lat_long(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        print("Latitude:", location.latitude)
        print("Longitude:", location.longitude)
    else:
        latitude, longitude = 0, 0
        print("Could not geocode the address.")
    return latitude, longitude
