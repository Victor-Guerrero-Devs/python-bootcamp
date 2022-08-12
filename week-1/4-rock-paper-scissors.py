import math
import random

random_num = math.floor(random.random() * 3)

choices = ['rock', 'paper', 'scissors']

# alternatively, you can just use the random method
# computer_choice = random.choice(choices)
computer_choice = choices[random_num]

print("Welcome to rock, paper, scissors.  Are you ready to play?")

player_choice = (input("Pick your weapon: rock, paper, or scissors: ")).lower()

if computer_choice == player_choice:
    print(f"Oh no, you both picked {player_choice}! Please try again.")

elif (computer_choice == 'rock' and player_choice == 'scissors') or (computer_choice == 'scissors' and player_choice == 'paper') or (computer_choice == 'paper' and player_choice == 'rock'):
    print(f"Oh no, you lost! the computer chose {computer_choice} and you chose {player_choice}")
else:
    print(f"Congratulations! You won! the computer chose {computer_choice} and you chose {player_choice}")
