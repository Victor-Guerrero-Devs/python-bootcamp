import random

words = ['root', 'sudo', 'way', 'back']

chosen_word = random.choice(words)
word_length = len(chosen_word)
display = []

for letter in chosen_word:
    display += '_'

print(f"the answer is {chosen_word}")
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)