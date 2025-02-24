from os import path
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt

import webscrape


# filename = "data/homegate.csv"
filename = "data/d.csv"

if not path.isfile(filename):
    w = webscrape.WebScrape(None, None)
    w.get_data(start_page=1, end_page=51, timeout=7, path=filename, show=True)

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

def assign_score(p, r, m, d):
    return p - r - m + d 
