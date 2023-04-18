import random


def start_game(difficulty):
    return 10 if difficulty == 'easy' else 5


def check_guess(guess, winning_number):
    if guess == winning_number:
        print(f"You won! {guess} is the winning number!")
        return True
    elif guess > winning_number:
        print(f"Try again. {guess} is too high")
    else:
        print(f"Try again. {guess} is too low")
    return False


def play_game():
    difficulty = input("Welcome, do you want to play easy or hard? ")
    attempts = start_game(difficulty)
    winning_number = random.randint(1, 100)

    while attempts > 0:
        guess = int(input("Guess a number: "))
        if check_guess(guess, winning_number):
            break
        attempts -= 1
        print(f"You have {attempts} attempt(s) left.")
    else:
        print(f"Sorry, you ran out of attempts. The winning number was {winning_number}")


play_game()
