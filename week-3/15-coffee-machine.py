espresso = {
    "water": 50,
    "coffee": 18,
    "milk": 0,
    "price": 1.5
}

latte = {
    "water": 200,
    "coffee": 24,
    "milk": 150,
    "price": 2.5
}

cappuccino = {
    "water": 250,
    "coffee": 24,
    "milk": 100,
    "price": 3
}

starting_resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}


def check_resources(product):
    if starting_resources["water"] < product["water"]:
        return "Not Enough Water"
    elif starting_resources["coffee"] < product["coffee"]:
        return "Not Enough Coffee"
    elif starting_resources["milk"] < product["milk"]:
        return "Not Enough Milk"
    else:
        return "Good to go!"


def deduct_resources(product):
    starting_resources["water"] -= product["water"]
    starting_resources["coffee"] -= product["coffee"]
    starting_resources["milk"] -= product["milk"]
    starting_resources["money"] += product["price"]


def order_drink():
    while True:
        order = input("What would you like? (espresso, latte, cappuccino): ")
        if order == 'latte':
            if check_resources(latte) == "Good to go!":
                deduct_resources(latte)
                print("Here's your latte. Enjoy!")
            else:
                print(check_resources(latte))
        elif order == 'espresso':
            if check_resources(espresso) == "Good to go!":
                deduct_resources(espresso)
                print("Here's your espresso. Enjoy!")
            else:
                print(check_resources(espresso))
        elif order == 'cappuccino':
            if check_resources(cappuccino) == "Good to go!":
                deduct_resources(cappuccino)
                print("Here's your cappuccino. Enjoy!")
            else:
                print(check_resources(cappuccino))
        else:
            print("Invalid selection, please try again.")
            continue
        another_order = input("Would you like to order something else? (y/n): ")
        if another_order == 'n':
            break


print("Welcome to the coffee shop.")
order_drink()
print(f"Remaining resources: {starting_resources}")
