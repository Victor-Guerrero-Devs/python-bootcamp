import random

words = ['root', 'sudo', 'way', 'back']

chosen_word = random.choice(words)

display = []

for letter in chosen_word:
    display += '_'
