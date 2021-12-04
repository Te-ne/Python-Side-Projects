import pandas as pd
import string
num=int(input("Enter the number you are checking for: "))
for i in range(2,num):
        while num > 1:
            if (num % i) == 0:
                print(num,"is not a prime number")
                num=int(input("Enter the number you are checking for: "))
            else:
                print(num,"is a prime number")
                num=int(input("Enter the number you are checking for: ")) 