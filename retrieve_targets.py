import requests
from bs4 import BeautifulSoup

class Targets:
    def __init__(self, page, price, rooms):
        self.page = page
        self.price = price
        self.rooms = rooms

        site_url = "https://www.homegate.ch/rent/apartment/city-zurich/matching-list"
        self.url = site_url + "?ep=" + str(page) + "&ac=" + str(rooms) + "&ipd=false" + "&ah=" + str(price)

        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        self.infos = self.soup.find_all("div", attrs={"class": "HgListingCard_info_RKrwz"})
        # self.infos = self.soup.find("div", attrs={"class": "HgListingCard_info_RKrwz"})

    def get_number_results(self):
        results_buttons = self.soup.find_all("span", attrs={"class": "HgButton_content_RMjt_"})

        for i in range(len(results_buttons)):
            if i == 1:
                str_results = str(results_buttons[i].string)
                break

        ans = ""
        for c in str_results:
            if c.isdigit():
                ans += str(c)

        self.n_results = int(ans)
        return self.n_results

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

    def get_info(self, show=None):
        targets = []

        for info in self.infos:
            price = self.get_price(info)
            rooms, meters = self.get_space(info)
            address = info.find("address", attrs={"translate": "no"}).get_text()

            t = dict(price=price, rooms=rooms, meters=meters, address=address)
            targets.append(t)

            if show == True:
                print(t)

        return targets

obj = Targets(None, 2000, 3)
obj.get_info(show=True)
