from art import logo
import random

def play_game():
  print(logo)
  print("Welcome to the number guessing game!")
  target = random.randint(1, 100)
  print(target)
  
  print("I'm thinking of a number between 1 and 100.")
  
  level = input("Choose a difficulty level. Enter 'h for 'hard' or 'e' for 'easy': ")
  if level == "h":
    tries = 5
  elif level == "e":
    tries = 10
  
  guess = int(input("Make a guess: "))
  tries -= 1
  
  while tries > 0:
    if guess > target:
      guess = int(input("Too high, guess again: "))
      tries -= 1
    elif guess < target:
      guess = int(input("Too low, guess again: "))
      tries -= 1
    elif guess == target:
      print("You guessed it. You win!")
      tries = -1
  
  if tries == 0:
    print("You ran out of tries, you lose.")

while input("Do you want to play 'Guess the number?' y/n\n") == "y":
  play_game()