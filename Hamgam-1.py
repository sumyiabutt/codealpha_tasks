# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:31:56 2026

@author: l1s24bscs0067
"""

import random

words = ["babar", "kohli", "rizwan", "afridi", "warner"]

word = random.choice(words)
guessed = []
wrong = 0

print("Welcome to Hangman")
print("Guess the cricket player's name.")
print("You have 6 wrong chances.")

while wrong < 6:

    display = ""

    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You guessed it!")
        break

    guess = input("Enter one letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed:
        print("You already entered this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong = wrong + 1
        print("Wrong guess.")
        print("You have used", wrong, "wrong chances.")

if wrong == 6:
    print("Game over.")
    print("The name was:", word)
