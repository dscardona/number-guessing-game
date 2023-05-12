# Welcome user to game
# from art import logo
# from replit import clear
import random

# print(logo)
print("Welcome to the number guessing game!")
# I'm thinking of a number between 1 and 100: randomly select a target number, save as target
target = random.randint(1, 100)
print(target)

print("I'm thinking of a number between 1 and 100.")

# Select level: hard or easy. if hard: 5 attempts if easy 10 attemps
level = input("Choose a difficulty level. Enter 'h for 'hard' or 'e' for 'easy': ")
if level == "h":
  tries = 5
elif level == "e":
  tries = 10

# Ask player to make a guess, compare to target, print clue, take input again if needed(loop)
guess = int(input("Make a guess: "))
tries -= 1

while tries > 0:
  if guess > target:
    guess = int(input("Too high, guess again: "))
    tries -= 1
  elif guess < target:
    guess = int(input("Too low, guess again: "))
    tries -= 1
  # if guess = target before tries expire: you win
  elif guess == target:
    print("You guessed it. You win!")
    tries = -1

# if tries expire: you lose
if tries == 0:
  print("You ran out of tries, you lose.")
  


#play again?
