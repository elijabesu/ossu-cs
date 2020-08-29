import string
import random

LETTERS = list(string.ascii_letters)
DIGITS = list(string.digits)
PUNCTUATION = list(string.punctuation)
NO = ["no", "false", "n", "f"]

def get_length():
    length = input("How many characters should your password have? ")

    return int(length)

def get_available_string():
    wanted = list()

    want_letters = input("Contain letters? ")
    if want_letters.lower() not in NO:
        wanted += LETTERS

    want_digits = input("Contain numbers? ")
    if want_digits.lower() not in NO:
        wanted += DIGITS

    want_punctuation = input("Contain punctuation? ")
    if want_punctuation.lower() not in NO:
        wanted += PUNCTUATION

    return wanted

def get_password():
    length = get_length()
    wanted = get_available_string()

    password = "".join(random.choices(wanted, k = length))
    return password

password = get_password()
print("Your new password is: \t\t" + password)
