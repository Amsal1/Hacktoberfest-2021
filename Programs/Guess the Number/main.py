from art import logo
from random import randint
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

answer = randint(1, 100)
chances_left = 0
quit_game = False
print(logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
	chances_left += 10
elif difficulty_level == "hard":
	chances_left += 5
else:
	print("Invalid Input You Lost!")

while chances_left > 0:
	user_guess = int(input("Make a guess: "))
	if user_guess > answer:
		print("Too high.")
		chances_left -= 1
		if not user_guess == answer:
			print("Guess again.")
			print(f"You Have {chances_left} Chances Left")
	elif user_guess < answer:
		print("Too low.")
		if not user_guess == answer:
			print("Guess again.")
			print(f"You Have {chances_left} Chances Left")
		chances_left -= 1
	elif user_guess == answer:
		print(f"You got it! The answer was {answer}")
		chances_left = 0
	if chances_left <= 0:
		print(f"You've run out of guesses, you lose. By The Way, The Answer was {answer}")

