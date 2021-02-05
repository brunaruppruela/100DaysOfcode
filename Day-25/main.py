#lendo a linha 3 do arquivo do diretorio day 24
# with open("./Day-25/weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

import csv

with open("./Day-25/weather_data.csv") as file:
    data = csv.reader(file)