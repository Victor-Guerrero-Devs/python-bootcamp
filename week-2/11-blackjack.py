import random


def hit(player):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    added_card = random.choice(cards)
    player.append(added_card)


def play_game():
    player_score = deal_hand()
    computer_score = deal_hand()

    while True:
        message = input(f"You currently have {player_score} and the total is {sum(player_score)}. Do you want to stay "
                        f"or hit? ")

        if message == "hit":
            hit(player_score)
            hit(computer_score)
            print(f"Your scores are now {player_score} and the total is {sum(player_score)}")
        elif message == "stay":
            break  # exit the loop and end the game
        else:
            print("Invalid input. Please enter 'stay' or 'hit'.")

    end_game(player_score, computer_score)


def deal_hand():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    return [random.choice(cards), random.choice(cards)]


def end_game(p_final, c_final):
    if p_final == []:
        print("Fine, don't play with us anymore")
        return

    player_total = sum(p_final)
    computer_total = sum(c_final)
    if computer_total > 21:
        print("You won! The computer went over 21")
    elif player_total > 21:
        print(f"You lost! You went over the limit: {player_total}")
    elif 21 - player_total < 21 - computer_total:
        print(f"You won! {player_total} vs {computer_total}")
    else:
        print(f"You lost! {player_total} vs {computer_total}")

    start_game()


def start_game():
    message = input("Do you want to play blackjack? (y/n) ")
    if message == 'y':
        play_game()
    else:
        end_game([], [])


start_game()