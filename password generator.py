#import pandas
import pandas as pd
import string
import secrets
import random
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation
#Welcome message
print("Hola! \nWelcome to Ten's password generator.")
#Add all elements of the password
all= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#Ask the user the desired length if their password
length = int(input("\nHow long would you want your password to be: "))
#Use .join to create the password and .choice for a random selection of characters with repetition allowed
password= " ".join(secrets.choice(all) for i in range(length))
while length < 6:
 print("Minimum password length is 6\nPlease increase the length of password.\n")
 length = int(input("How long would you want your password to be: "))
print(password)
