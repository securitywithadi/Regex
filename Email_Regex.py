import re

#Defining a regular Expression to match an Email ID

email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

#Receive User input

email = input("Enter your email address: ")

#Checking if the email matches the Regex Pattern

if re.match(email_regex, email):
    print("Email is Valid")

else:
    print("Invalid Email Address")