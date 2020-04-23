#! python3

import random

print('Hello. What is your name? ')
name = input()
print('Well, {0}, I am thinking of a number between 1 and 20'.format(name))

secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print('Take a guess ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This condition is for the correct guess!

if guess ==secretNumber:
    print('It took you {0} guesses'.format(str(guessesTaken)))
else:
    print('Nope. That was not the number {0}. The number was {1}'.format(name,
        str(secretNumber)))
