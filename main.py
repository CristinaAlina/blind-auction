from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
continue_bid = True


def find_the_highest_bid(bids):
    winner_name = max(bids, key=bids.get)
    winner_bid = bids[winner_name]
    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")


while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid

    response = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    clear()  # clear the output in the console

    if response == 'no':
        continue_bid = False
        find_the_highest_bid(bidders)
