# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:25:10 2023

@author: rushilsheth
"""

import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by selecting random characters from the set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Get the desired length of the password from the user
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(password_length)

# Print the password
print("Your password is:", password)
