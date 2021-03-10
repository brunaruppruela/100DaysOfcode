from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = 
PASSWORD = 

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

#Leitura do csv contendo os dados dos aniversariantes
data = pandas.read_csv("./Day-32/birthdays.csv")
#criando um dicionario comprehension com o csv para leitura do mes e dia, 
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"./Day-32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
        """retirando o bug UnicodeEncodeError: 'ascii' codec can't encode characters in position 57-58: ordinal not in range(128), usando o encode para
        ignorar o erro"""
        contents.encode('ascii', 'ignore').decode('ascii')
        msgFrom = birthdays_person["email"]
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(MY_EMAIL, PASSWORD)
        smtpObj.sendmail(MY_EMAIL,msgFrom, "Subject: Feliz Aniversario\n{}".format(contents))
        smtpObj.quit()
        print("Email enviado com sucesso!")  


#não funcionou, da erro de latencia para liberar o smtp do gmail
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    # #metodos de segurança dos emails
    #     connection.starttls()
    #     connection.login(MY_EMAIL, PASSWORD)
    #     connection.sendemail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=birthdays_person["email"],
    #         msg=f"Subject: Feliz Aniversario!\n\n{contents}"
    #     )