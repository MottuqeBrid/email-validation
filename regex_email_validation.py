# Email validation using regex in python

import re

# user_email = input("Enter your email: ")


def check_email(email):
    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(email_condition, email):
        print("Valid email")
    else:
        print("Invalid email")


while True:
    print("Enter 'exit' to exit the program")
    email = input("Enter your email: ")
    if email == "exit":
        break
    else:
        check_email(email)
