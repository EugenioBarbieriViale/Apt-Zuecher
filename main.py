from os import path

import pandas as pd
import matplotlib.pyplot as plt

from geopy.geocoders import Nominatim
from geopy import distance

import webscrape


filename = "homegate.csv"

if not path.isfile(filename):
    w = webscrape.WebScrape(None, None)
    w.get_data(start_page=1, end_page=51, timeout=10, path=filename, show=True)

def get_coordinates(address):
    geolocator = Nominatim(user_agent="myapp")

    target = geolocator.geocode(address)
    destination = geolocator.geocode("Rämistrasse 101 8092 Zurich")

    gps_targ = (target.latitude, target.longitude)
    gps_dest = (destination.latitude, destination.longitude)

    distance = distance.geodesic(gps_dest, gps_targ).km
    return round(distance, 2)

prices = pd.read_csv(filename, usecols=["price"]).values
rooms = pd.read_csv(filename, usecols=["rooms"]).values
meters = pd.read_csv(filename, usecols=["meters"]).values
addresses = pd.read_csv(filename, usecols=["address"]).values

def show_graph():
    plt.title("Apartments from homegate.ch")
    plt.xlabel("Meter per square (m^2)")
    plt.ylabel("Price (CHF)")

    plt.scatter(meters, prices)
    plt.show()

show_graph()
