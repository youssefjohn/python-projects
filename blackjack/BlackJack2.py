import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return " Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)

    user = []
    computer = []
    is_game_over = False

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())



    while not is_game_over:

        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"   Your cards: {user}, current score: {user_score}")
        print(f"   Computers first card: {computer[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' for another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"     Your final hand was: {user}, final score: {user_score}")
    print(f"     Computers final hand was: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play another game of BlackJack? y/n: ") == 'y':
    play_game()
