
with open("./Day-25/weather_data.csv", "r") as file:
    data = file.readlines()
    print(data)
import csv
#abrindo o arquivo da mesma estrutura de arquivos de trabalho
with open("./Day-25/weather_data.csv") as file:
    #armazenando a leitura em data
    data = csv.reader(file)
    #lista vazia para receber somente as temperaturas da coluna  temperatura da planilha
    temperatures = []
    #loop for para percorrer cada linha do arquivo csv
    for linha in data:
        #condicao para achar o label temp do arquivo e não considera-lo, apenas preencher a lista convertida pra int em temperatures
        if linha[1] != "temp":
            temperatures.append(int(linha[1]))
    print(temperatures)

import pandas
#lendo o arquivo csv e printando a coluna temp
data = pandas.read_csv("./Day-25/weather_data.csv")
print(data["temp"])

#transformando o data lido na linha 21 em um dicionario chamado data_dict
data_dict = data.to_dict()
print(data_dict)

#Calcular media de valores da coluna temperatura com python e com a funcao mean do pandas
temp_list = data["temp"].to_list()
print("A media de Temperatura e: ", int(sum(temp_list) / len(temp_list)))
print("A media e: ", data["temp"].mean())
#Calcular valor maximo da coluna tempo
print("O valor maximo e: ", data["temp"].max())

#Get Data in columns
print(data["condition"]) 
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) #ou print(data[data.temp == data.temp.max()] )

monday = data[data.day == "Monday"]
print(monday.condition)

temperatura = data.temp
print("Temperatura em Fahrenheit:")
print((temperatura * 9/5) + 32)

# Formula de conversao do ºC par ºF
# (0 °C × 9/5) + 32

#Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
#cria um novo arquivo csc armazenando os valores data recebidos da transformação do data_dict em um dataframe
data.to_csv("new_dat.csv")
