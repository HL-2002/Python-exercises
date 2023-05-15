""" 
In a file called game.py, implement a program that:

* Prompts the user for a level, n. If the user does not input a positive integer, 
the program should prompt again.
* Randomly generates an integer between 1 and n, inclusive, using the random module.
* Prompts the user to guess that integer. If the guess is not a positive integer, 
the program should prompt the user again:
    - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    - If the guess is the same as that integer, the program should output Just right! and exit.
"""

from random import randint
import sys

# Input of level
while True:
    try:
        n = int(input("Level: ")) # ValueError
    except ValueError:
        print("Please input a positive integer...\n")
    else:
        if n > 0:
            break
        else:
            print("Please input a positive integer...\n")
print()

# Generating number to guess
number = randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("Please input a positive integer...\n")
    else:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too big!")
        else:
            print("Just right!")
            sys.exit()