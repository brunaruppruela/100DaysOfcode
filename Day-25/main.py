
import pandas

data = pandas.read_csv("./Day-25/squirrel.csv")

#printando a coluna de cores
#print(data["Primary Fur Color"]) 

#gray = data[data["Primary Fur Color"] == "Gray"]
#capturando o tamanho de cada cor de esquilo do dataframe e contando a quantidade de cada
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)
print(red_count)
print(black_count)

#criando um novo arquivo e inserindo os novos dados de cores captuados 
data_dict = {
    """as chaves serao as colunas do novo CSV, os valores serao buscado das variaveis de armazanemanto"""
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]

}
#utilizando a funcao DataFrame para transformar o o dicionario data_dict em um novo csv color_squirrel.csv
data = pandas.DataFrame(data_dict)
data.to_csv("color_squirrel.csv")
