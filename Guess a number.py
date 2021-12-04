import pandas
import string
import random
num = random.randrange(1,50)
guess = int(input("Hola!\nWhat's your guess? : "))
while guess != num:
    if guess > num:
        print("Your guess is too high, try a lower number")
        guess = int(input("\nGuess a number "))
    else:
        print("Your guess is too low, try a higher number")
        guess = int(input("\nGuess a number "))
if guess == num:
    print("Yay!\nYou have guessed correctly\nCiao!")