import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_char = letters + numbers + symbols

passwords = []

while True:
    choice = int(input("Enter 1 for generate a new password, 2 for show generated password, 3 for delete a password, " \
    "4 for end: "))
    if choice == 1:
        length = int(input("Enter the length of the password you would like to randomly generate: "))
        password = ""
        for i in range(length):
            password += random.choice(all_char)
        passwords.append(password)
    elif choice == 2:
        index = int(input("Enter number of the password you would like to show: "))
        if len(passwords) < index or index < 1 :
            if len(passwords) == 1:
                print("There is only 1 password")
            else:
                print(f"There are olny {len(passwords)} passwords")
        else:
            print(f"Generated password: {passwords[index - 1]}")
    elif choice == 3:
        index = int(input("Enter number of password you would like to delete: "))
        if len(passwords) < index or index < 1:
            print(f"There are only {len(passwords)} passwords")
        else:
            passwords.pop(index - 1)
    elif choice == 4:
        break
