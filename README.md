# Find apartments in Zurich
This python program collects information from 1000 apartments using a swiss site called ["homegate.ch"](homegate.ch/) through webscraping. It gathers price, square meters, number of rooms and address of every apartment. It also calculates the distance from the ETH main building by getting the GPS coordinates, using the address. \\
To every apartment is then assigned a score, which is based on the four featurs named above. The ranking of the best apartments is made of the ones with lower score.

## Dependencies
- numpy
- pandas
- csv
- matplotlib
- requests
- beautifulsoup4
- geopy
