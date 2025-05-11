# Find apartments in Zurich to study at ETH
This python program collects data of 1000 apartments using a Swiss site called ["homegate.ch"](homegate.ch/) by webscraping. It gathers price, square meters, number of rooms and address of every apartment. It also calculates the distance from the ETH main building by using the address and getting its GPS coordinates.

To every apartment is then assigned a score, which is based on the four features named above (price, square meters, rooms and distance). The ranking of the best apartments is made out of the ones with lowest score.

Here you can find both the scripts and a csv file in which the data is saved.

## Dependencies
- numpy
- pandas
- csv
- matplotlib
- requests
- beautifulsoup4
- geopy


The data was gathered in February 2025
