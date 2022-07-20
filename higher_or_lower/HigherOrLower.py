import random
from game_data import data
from art import logo, vs


def game():

    # Show logo
    print(logo)

    def comparison_data(person):
        """Pulls a random object from a dictionary, then makes sure it is not the same object
        as the original object(person), if it is, then pull out another random object instead"""
        person_b = random.choice(data)
        # Check that they aren't the same object from game_data
        if person['name'] == person_b['name']:
            person_b = random.choice(data)
        return person_b


    user_score = 0

    # Pick person from game_data to be current subject
    person_a = random.choice(data)
    # Pick another object to compare against person_a
    person_b = comparison_data(person_a)

    end_game = False
    while not end_game:
        print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}")
        print(vs)
        print(f"Compare B: {person_b['name']}, a {person_b['description']} from {person_b['country']}")

        choice = input("Which one has more followers, 'A' or 'B': ").lower()

        if choice == 'a':
            if person_a['follower_count'] > person_b['follower_count']:
                user_score += 1
                print(f"You're right! You're current score is: {user_score}")
                person_a = person_b
            else:
                print("You lost!")
                end_game = True
        elif choice == 'b':
            if person_b['follower_count'] > person_a['follower_count']:
                user_score += 1
                print(f"You're right! You're current score is: {user_score}")
                person_a = person_b
            else:
                print("You lost!")
                end_game = True


        person_b = comparison_data(person_a)

    play_again = input("Would you like to play again? y/n ").lower()
    if play_again == 'y':
        game()
    else:
        print("Take Care")

game()




# Pick person from game data to compare against subject
    # Ask user to pick which one has more followers, if correct:
        # person > subject, subject = person
    # else: user loses
#
# def comparison_data(person_a):
#
#     person_b = random.choice(data)
#     # Check that they arent the same object from game_data
#     if person_a['name'] == person_b['name']:
#         person_b = random.choice(data)
#     return person_b
# #
#
# def make_comparison(person_a, score):
#     random_choice = comparison_data(person_a)
#     print(f"Compare B: {random_choice['name']}, a {random_choice['description']} from {random_choice['country']}")
#     choice = input("Which one has more followers, 'A' or 'B': ").lower()
#
#     if choice == 'b':
#         if random_choice['follower_count'] > person_a['follower_count']:
#             person_a = random_choice
#             score += 1
#         else:
#             print("Sorry thats incorrect, you lose")
#             return
#     elif choice == 'a':
#         if person_a['follower_count'] > random_choice['follower_count']:
#             person_a = random_choice
#             score += 1
#         else:
#             print("Sorry thats incorrect, you lose")
#             print(f"Final score {score}")
#             return
#
#
#     # If user choice > other choice
#     # user_score += 1 and user choice = other choice
#     # else: tell user that they lose
#
#
# make_comparison(person_a, user_score)
#
#
#
