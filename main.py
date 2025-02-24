from os import path
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt
from numpy import array, argsort

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

if not path.isfile(dist_file):
    w = webscrape.WebScrape(None, None)
    w.write_distances(addresses, path=dist_file, timeout=1.1, show=True)

distances = pd.read_csv(dist_file, usecols=["distance"]).values

def price_meters_graph():
    plt.title("Apartments from homegate.ch")
    plt.xlabel("Square meters (m^2)")
    plt.ylabel("Price (CHF)")

    plt.scatter(meters, prices)
    plt.show()

def price_dist_graph():
    plt.title("Apartments from homegate.ch")
    plt.xlabel("Distance from ETH (km)")
    plt.ylabel("Price (CHF)")

    plt.scatter(distances, prices)
    plt.show()


def loss(p, m, r, d):
    if p != 0.0 and m != 0.0:
        return p / m 
    return 10.0

limit_price = 4000
limit_rooms = 3.0

targets = []
for i in range(len(prices)):
    if prices[i] <= limit_price and rooms[i] >= limit_rooms:
        targets.append([prices[i], meters[i], rooms[i], addresses[i], distances[i]])

max_price = max(targets[1:])[0][0]
max_meter = max(targets[1:])[1][0]
max_room = max(targets[1:])[2][0]
max_distance = max(targets[1:])[4][0]
# print(max_price, max_meters, max_rooms, max_distances)

scores = []
for i in range(len(targets)):
    p = float(targets[i][0][0]) / float(max_price)
    m = float(targets[i][1][0]) / float(max_meter)
    r = float(targets[i][2][0]) / float(max_room)
    d = float(targets[i][4][0]) / float(max_distance)

    score = loss(p, m, r, d)
    scores.append(score)

np_scores = array(scores)
sorted_indices = np_scores.argsort()
# sorted_scores = np_scores[sorted_indices]

# scores = list(enumerate(scores))
# scores.sort(key=lambda:x[1])

for i in reversed(range(10)):
    best_apartment = targets[sorted_indices[i]]
    print(best_apartment[0][0], best_apartment[1][0], best_apartment[2][0], best_apartment[3][0])
