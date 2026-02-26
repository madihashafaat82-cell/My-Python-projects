import random

secret_number = random.randint(1,100)

print('Guess a number between 1 to 100.')

guess = int(input("Write your Guess number:"))

if guess==secret_number:
    print('Great your answer is correct.')
else:
    print('Your answer is not correct.')
    print("Try again!")
