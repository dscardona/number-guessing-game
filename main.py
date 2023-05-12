# Welcome user to game
from art import logo
import random

print(logo)
print("Welcome to the number guessing game!")
# I'm thinking of a number between 1 and 100: randomly select a target number, save as target
target = random.randint(1, 100)
print(target)

print("I'm thinking of a number between 1 and 100.")

# Select level: hard or easy. if hard: 5 attempts if easy 10 attemps
level = input("Choose a difficulty level. Enter 'h for 'hard' or 'e' for 'easy': ")
if level == "hard":
  tries = 5
else:
  tries = 10

# Ask player to make a guess, compare to target, print clue, take input again (loop)
# if tries expire: you lose
# if guess = target before tries expire: you win
#play again?
