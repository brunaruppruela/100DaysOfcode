from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "brunarupp@gmail.com"
PASSWORD = 

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./Day-32/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"./Day-32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contentes = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
    #metodos de segurança dos emails
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendemail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject: Feliz Aniversario!\n\n{contents}"
        )