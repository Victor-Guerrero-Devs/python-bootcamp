print("Welcome to Treasure Island!\nYour mission is to find the treasure!")

answer1 = input("You come to a crossroads. Do you go left or right?")

if answer1 == 'left':
    print("Game over. You have encountered a pack of wolves that have eaten you.")
    exit()
else:
    print("You have reached a river.")

answer2 = input("Do you wish to swim or wait?")

if answer2 == 'swim':
    print("Game over. A shark has eaten you!")
    exit()
else:
    print("A fairy has appeared and presented you with three gifts!")

answer3 = input("Do you choose the red or yellow or green one?")

if answer3 == 'red':
    print("BOOM! Game over. It was a bomb!")
    exit()
elif answer3 == 'yellow':
    print("ACK! Game over. It was poison!")
    exit()
else:
    print("Congratulations! You have choosen correctly and have recieved the treasure!")
