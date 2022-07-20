from art import logo

print(logo)
print("Welcome to the Secret Auction program!")

potential_buyers = {}
keep_bidding = True


def auction_outcome(person, bid_amount):

    potential_buyers[person] = bid_amount

    highest_bid = 0
    name_of_winner = ""
    for key in potential_buyers:
        if potential_buyers[key] > highest_bid:
            highest_bid = potential_buyers[key]
            name_of_winner = key

    return name_of_winner, highest_bid


while keep_bidding:
    name = input("What is your name? ").lower()
    amount = int(input("How much would you like to bid? "))

    winner, bid = auction_outcome(person=name, bid_amount=amount)

    keep_playing = input("Would you like to keep playing? Yes or No: ").lower()
    if keep_playing != 'yes':
        print(winner)
        print(potential_buyers)
        keep_bidding = False
