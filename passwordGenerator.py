import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891234567890!@#$%^&*()"

while True:
    passwordLength = int(input("What is the length of your desired password: "))
    passwordCount = int(input("How many passwords would you like: "))
    for x in range(0, passwordCount):
        print(x)