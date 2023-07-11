import random
import string
import secrets
list_upper = list(string.ascii_uppercase)
list_lower = list(string.ascii_lowercase)
list_number = list(string.digits)
list_specchar = list(string.punctuation)

random.shuffle(list_upper)
random.shuffle(list_lower)
random.shuffle(list_number)
random.shuffle(list_specchar)
len_chars = int(input("Enter The number of length of No. At least 6 chars : "))
password = []
if(len_chars >= 6):
    for i in range(len_chars):
        cryp = secrets.choice(list_upper + list_lower + list_number + list_specchar)
        password.append(cryp)
else:
    print("you need at least a 6 characters")
password = "".join(password[0:])
print(password)