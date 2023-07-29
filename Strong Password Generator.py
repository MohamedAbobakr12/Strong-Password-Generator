import random
import string

"""
This code generates a random string of a specified length.

The user is prompted to enter the length of the random string.
The code then generates a random string of the specified length using a combination of uppercase letters, lowercase letters, punctuation marks, and numbers.
The random string is then printed to the console.

Usage:

python random_string.py

This will prompt you to enter the length of the random string.
The code will then generate a random string of the specified length and print it to the console.

"""

upper = string.ascii_uppercase
lower = string.ascii_lowercase
punc = string.punctuation
num = string.digits

length = int(input("Enter The Length: "))
all_letter = upper + lower + punc + num

password = "".join(random.sample(all_letter, length))
print(password)
