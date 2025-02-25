# Find apartments in Zurich to study at ETH
This python program collects information of 1000 apartments using a swiss site called ["homegate.ch"](homegate.ch/) through webscraping. It gathers price, square meters, number of rooms and address of every apartment. It also calculates the distance from the ETH main building by getting the GPS coordinates, using the address.

To every apartment is then assigned a score, which is based on the four features named above (price, square meters, rooms and distance). The ranking of the best apartments is made out of the ones with lowest score.

## Dependencies
- numpy
- pandas
- csv
- matplotlib
- requests
- beautifulsoup4
- geopy


The data was gathered in February 2025
