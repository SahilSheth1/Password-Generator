# Import libraries

import random

# Variable that stores all the possible characters for password generation

characters = "abcdefghijklmnopqrstuvwxyz1234567891234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891234567890!@#$%^&*()"

# Prompts for User input

passwordLength = int(input("What is the length of your desired password: "))
passwordCount = int(input("How many passwords would you like: "))

# First part of output

print("Passwords: \n")

# Loops to generate passwords

for x in range(0, passwordCount):
    password = ""
    
    for y in range(0, passwordLength):
        
        # Function to randomly select a character from the characters variable
        
        passwordCharacter = random.choice(characters)
        password = password + passwordCharacter
    
    # Print out the passwords
        
    print(password, "\n")