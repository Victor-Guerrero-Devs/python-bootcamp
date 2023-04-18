bidders_list = []

def get_bid():
    name = input("Enter your name: ")
    bid = input("Enter your bid: $")
    bidders_list.append({"name": name, "bid": int(bid)})


def get_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        if bid["bid"] > highest_bid:
            highest_bid = bid["bid"]
            winner = bid["name"]
    return f"{winner} has won with a bid of ${highest_bid}"


while True:
    get_bid()
    more_bidders = input("Are there more bidders? (yes/no): ")
    if more_bidders.lower() == "no":
        break

winner = get_highest_bid(bidders_list)
print(winner)
