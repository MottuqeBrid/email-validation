# Email validation Using python


# email = input("Enter your email: ")  # g@g.in


def check_email(email):
    k, j, d = 0, 0, 0
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and email.count("@") == 1:
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                            break
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "@" or i == "." or i == "_":
                            continue
                        else:
                            d = 1
                            break
                    if k == 1 or j == 1 or d == 1:
                        print("Wrong email format 7")
                    else:
                        print("Valid email")

                    if k == 1 or j == 1:
                        print("Wrong email format 5")
                else:
                    print("Wrong email format 4")
            else:
                print("Wrong email format 3")
        else:
            print("Wrong email format 2")
    else:
        print("Wrong email format 1")


while True:
    print("Enter 'exit' to exit the program")
    email = input("Enter your email: ")
    if email == "exit":
        break
    else:
        check_email(email)
