import string
import random

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = string.punctuation

CHARACTERS = LETTERS + DIGITS + SYMBOLS

def generate_password(length: int = 20):
    password = "".join(random.choice(CHARACTERS) for i in range(length))
    
    return password
