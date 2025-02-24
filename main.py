from os import path
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt

import webscrape


filename = "data/homegate.csv"

if not path.isfile(filename):
    w = webscrape.WebScrape(None, None)
    w.write_data(start_page=1, end_page=51, timeout=7, path=filename, show=True)

prices = pd.read_csv(filename, usecols=["price"]).values
rooms = pd.read_csv(filename, usecols=["rooms"]).values
meters = pd.read_csv(filename, usecols=["meters"]).values
addresses = pd.read_csv(filename, usecols=["address"]).values

dist_file = "data/distances.csv"

# if not path.isfile(dist_file):
#     w = webscrape.WebScrape(None, None)
#     w.write_distances(addresses, path=dist_file, timeout=8, show=True)


def show_graph():
    plt.title("Apartments from homegate.ch")
    plt.xlabel("Square meters (m^2)")
    plt.ylabel("Price (CHF)")

    plt.scatter(meters, prices)
    plt.show()

show_graph()
