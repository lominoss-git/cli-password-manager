import string
import random
import pyperclip
from termcolor import colored

def generate_password(length):
    if input("• Should your password contain lowercase letters {}? [y/N] ".format(colored("abcd", "magenta"))) == "y":
        lowercase_letters = string.ascii_lowercase

    else:
        lowercase_letters = ""

    if input("• Should your password contain uppercase letters {}? [y/N] ".format(colored("ABCD", "magenta"))) == "y":
        uppercase_letters = string.ascii_uppercase

    else:
        uppercase_letters = ""

    if input("• Should your password contain numbers {}? [y/N] ".format(colored("1234", "magenta"))) == "y":
        numbers = string.digits

    else:
        numbers = ""

    if input("• Should your password contain symbols {}? [y/N] ".format(colored("§/.£", "magenta"))) == "y":
        symbols = string.punctuation

    else:
        symbols = ""

    characters = lowercase_letters + uppercase_letters + numbers + symbols

    if characters == "":
        print("Your password must contain at least one type of character! Try again.")
        
    else:
        password = "".join(random.choice(characters) for i in range(length))        
        print(colored(password, "red"))

        pyperclip.copy(password)
        print("Password copied to the clipboard!")
        
generate_password(int(input("How many characters should your password contain? ")))
