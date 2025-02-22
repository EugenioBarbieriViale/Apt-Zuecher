import requests
from bs4 import BeautifulSoup

class Targets:
    def __init__(self, page, price, rooms):
        self.page = page
        self.price = price
        self.rooms = rooms

        site_url = "https://www.homegate.ch/rent/apartment/city-zurich/matching-list"
        self.url = site_url + "?ep=" + str(page) + "&ac=" + str(rooms) + "&ipd=false" + "&ah=" + str(price)

    def reach_site(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")

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

        # print(ans)
        self.n_results = int(ans)
        return self.n_results

    def get_prices(self):
        prices = self.soup.find_all("span", attrs={"class": "HgListingCard_price_JoPAs"})

        ans = []
        for line in prices:
            chunk = []
            for c in line.get_text():
                if c.isdigit():
                    chunk.append(c)
            ans.append("".join(chunk))

        # print(f"Found {len(ans)} results:", ans)
        return ans 

    def get_space(self):
        space = self.soup.find_all("div", attrs={"class": "HgListingRoomsLivingSpace_roomsLivingSpace_GyVgq"})
        
        ans = []
        for line in space:
            chunk = []
            for elem in line.find_all("strong"):
                chunk.append(elem.get_text())
            ans.append(chunk)
        # print(f"Found {len(ans)} results:", ans)
        return ans

    def get_address(self):
        addr = self.soup.find_all("address", attrs={"translate": "no"})
        ans = []
        for a in addr:
            ans.append(a.get_text())

        # print(f"Found {len(ans)} results:", ans)
        return ans

    def targets(self):
        p = self.get_prices()
        s = self.get_space()
        a = self.get_address()

        self.targets = []
        # for i in range(self.n_results):
        for i in range(len(s)):
            self.targets.append(dict(price=p[i], space=s[i], addr=a[i]))

        return self.targets
        
obj = Targets(None, 2000, 3)
obj.reach_site()
obj.get_number_results()

for i in obj.targets():
    print(i)
