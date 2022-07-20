
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random


def game():

    end_game = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    players = {'user': [], 'computer': []}

    # Give the user and computer two random cards each
    players["user"].extend(random.choices(cards, k=2))
    players["computer"].extend(random.choices(cards, k=2))

    while not end_game:


        def get_card_computer(dictionary, player):
            """Take a dictionary and a key(computer), check that the sum is
            Greater than 17. If it isnt, then add another card until the total is
            more than 17.
            """

            if sum(dictionary[player]) < 17:
                while sum(dictionary[player]) < 17:
                    dictionary[player].append(random.choice(cards))


        def get_card(dictionary, player):
            """Ask the player if they would another card. If they dont want a card,
            then stop asking them, and continue the game. If they do want a card,
            then append a random card to their list, and ask them the same question again."""


            answer = input("Would you like another card? Y/N").lower()
            if answer == 'y':
                dictionary[player].append(random.choice(cards))
                print(f"Your cards are: {dictionary[player]}")




        def remove_and_append(dictionary, key_item, old_number, new_number):
            """Removes the number you dont want from the users list/deck, and then adds
            a new number to the end of their list/deck."""

            dictionary[key_item].remove(old_number)
            dictionary[key_item].append(new_number)


        def calculate_players_cards(dictionary):
            """Takes a dictionary and then checks whether the user/computer has hit the target of 21.
            If either of them have not, it then checks to see what their sums are."""


            for key, value in dictionary.items():
                if sum(value) == 21:
                    print(f"{key} is the winner!")

                elif sum(value) > 21:
                    if 11 in value:
                        remove_and_append(dictionary=dictionary, key_item=key, old_number=11, new_number=1)
                        if sum(value) > 21: #and 11 in value:
                            print(f"{key}'s has gone over 21. They lose!")


                        else:
                            print(f"{key}'s card are {value}, total is: {sum(value)}")
                    else:
                        print(f"{key} has gone over 21. They lose!")
                else:
                    print(f"{key}'s card are {value}, total is: {sum(value)}")
                    get_card(dictionary=dictionary, player='user')
                    get_card_computer(dictionary=dictionary, player='computer')


        winner = calculate_players_cards(players)
        end_game = True

game()


























#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

