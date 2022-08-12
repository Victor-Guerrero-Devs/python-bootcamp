import random

words = ['root', 'sudo', 'way', 'back']

chosen_word = random.choice(words)

display = []

for letter in chosen_word:
    display += '_'

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
