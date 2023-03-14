import random

characters = "abcdefghijklmnopqrstuvwxyz1234567891234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891234567890!@#$%^&*()"

passwordLength = int(input("What is the length of your desired password: "))
passwordCount = int(input("How many passwords would you like: "))

print("Passwords: \n")

for x in range(0, passwordCount):
    password = ""
    
    for y in range(0, passwordLength):
        passwordCharacter = random.choice(characters)
        password = password + passwordCharacter
        
    print(password, "\n")