import string
import random

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    char_set = ""
    if uppercase:
        char_set += string.ascii_uppercase
    if lowercase:
        char_set += string.ascii_lowercase
    if digits:
        char_set += string.digits
    if symbols:
        char_set += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(char_set)

    return password

length = int(input("enter password length: "))
uppercase = input("include uppercase letters? (y/n): ").lower() == "y"
lowercase = input("include lowercase letters? (y/n): ").lower() == "y"
digits = input("include digits? (y/n): ").lower() == "y"
symbols = input("include special symbols? (y/n): ").lower() == "y"

# Generate the password and print it
password = generate_password(length, uppercase, lowercase, digits, symbols)
print("generated password:", password)
