import requests
from time import sleep
from bs4 import BeautifulSoup
from csv import writer

class WebScrape:
    def __init__(self, price, rooms):
        self.price = price
        self.rooms = rooms

        self.site_url = "https://www.homegate.ch/rent/apartment/city-zurich/matching-list"

        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def reach_site(self, page):
        url = self.site_url + "?ep=" + str(page) + "&ac=" + str(self.rooms) + "&ipd=false" + "&ah=" + str(self.price)
        s = requests.Session()

        try:
            r = s.get(url, headers=self.headers)
            print(r)

        except requests.exceptions.Timeout as ex:
            print("Exception raised: ", ex)

        self.soup = BeautifulSoup(r.content, "html.parser")
        self.infos = self.soup.find_all("div", attrs={"class": "HgListingCard_info_RKrwz"})

    def get_space(self, info):
        space = info.find("div", class_="HgListingRoomsLivingSpace_roomsLivingSpace_GyVgq").get_text()

        rooms = []
        for i in range(len(space)):
            if i <= 4:
                if space[i].isdigit() or space[i] == ".":
                    rooms.append(space[i])
            else:
                rooms = "".join(rooms)
                break

        meters = []
        for i in range(8, len(space)):
            if space[i].isdigit() or space[i] == "m" or space[i] == "²":
                meters.append(space[i])

        meters = "".join(meters)

        return rooms, meters

    def get_price(self, info):
        price = info.find("span", class_="HgListingCard_price_JoPAs").get_text()[4:10]

        if price == "ce on ":
            return "Price on request" 

        return price

    def page_targets(self, show=None):
        targets = []

        for info in self.infos:
            price = self.get_price(info)
            rooms, meters = self.get_space(info)
            address = info.find("address", attrs={"translate": "no"}).get_text()

            # t = dict(price=price, rooms=rooms, meters=meters, address=address)
            t = [price, rooms, meters, address]
            targets.append(t)

            if show == True:
                print(t)

        return targets

    def get_data(self, n_pages, timeout, show=None):
        data = [
            ["price", "rooms", "meters", "address"]
        ]

        for page in range(n_pages):
            print(f"\n------- PAGE NUMBER {page} -------")

            self.reach_site(page)
            pt = self.page_targets(show=show)
            data.append(pt)

            sleep(timeout)

        path = "data.csv"
        with open(path, mode="w", newline="") as file:
            w = writer(file)
            w.writerows(data)

        print(f"CSV file '{path}' created successfully")
