import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = ""  # Enter your email
MY_PASSWORD = ""  # Enter your password

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)

# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr="MY_EMAIL",
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday\n\n{contents}")
