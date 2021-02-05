
import pandas

data = pandas.read_csv("./Day-25/squirrel.csv")

#printando a coluna de cores
#print(data["Primary Fur Color"]) 

#gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)
print(red_count)
print(black_count)

data_dict = {
    
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]

}

data = pandas.DataFrame(data_dict)
data.to_csv("color_squirrel.csv")
