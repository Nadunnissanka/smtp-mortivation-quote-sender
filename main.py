import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", mode="r") as file:
        quote = file.readlines()
    random_quote = random.choice(quote)

    my_email = "nadunnissanka@yahoo.com"
    my_password = "kbbzybtjgoqlrvsp"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nadunnissankauiux@gmail.com",
            msg=f"Subject:Daily Motivation!\n\n{random_quote}"
        )