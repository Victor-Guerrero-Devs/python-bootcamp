import random

words = ['root', 'sudo', 'way', 'back']

chosen_word = random.choice(words)
word_length = len(chosen_word)

display = []
for letter in chosen_word:
    display += '_'

print(f"the answer is {chosen_word}")
print(display)

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lost")

    if "_" not in display:
        end_of_game = True
        print("You win!")