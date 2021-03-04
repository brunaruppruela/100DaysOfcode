import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "brunarupp@gmail.com"
PASSWORD = 

if weekday == 1:
    with open(".\Day-32\Start\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

#usando o with para adicionar o provedor de email
with smtplib.SMTP("smtp.gmail.com") as connection:
    #metodos de segurança dos emails
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendemail(
            from_addr=MY_EMAIL,
            to_addrs="brunarupp@gmail.com",
            msg=f"Subject: Meu primeiro email em python hihi\n\n{quote}"
        )

