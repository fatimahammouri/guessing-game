"""A number-guessing game."""
import random

# Put your code here
player_name = input ("Howdy, what's your name?")
print(f"Hi {player_name} Welcome to the Guessing game")
random_number = int(random.randint(1, 100))
#print(random_number)  this is to show what random number was generated 
print (player_name + " ,I'm thinking of a number between 1 and 100.\nTry to guess my number.")

number_attempts = 0


while True:
    guessed_number = input ("what is your guess? ")
    number_attempts += 1 
    if guessed_number == random_number:
        print(f"Well done, {player_name}! You found my number in {number_attempts} tries!")
    
    if guessed_number > random_number:
        print("you're guess is too high")
        int(input())

        continue

