from geopy.geocoders import Nominatim
from geopy import distance

import webscrape

geolocator = Nominatim(user_agent="myapp")

destination = geolocator.geocode("ETH Zurich")
target = geolocator.geocode("Pilatusstrasse 7, 8032 Zürich")

gps_dest = (destination.latitude, destination.longitude)
gps_targ = (target.latitude, target.longitude)

distance = distance.geodesic(gps_dest, gps_targ).km

print(distance)

w = webscrape.WebScrape(None, None)
w.get_data(1, 1.5, show=True)
