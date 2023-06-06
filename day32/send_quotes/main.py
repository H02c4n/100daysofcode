import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

subject = "Email subject"
sender = "sender@gamil.com"
recipients = ["recipient@gmail.com"]
password = "password"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as quote_file:
        all_quotes =quote_file.readlines()
        quote = random.choice(all_quotes)

    msg = MIMEText(quote)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(sender, password)
        connection.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
