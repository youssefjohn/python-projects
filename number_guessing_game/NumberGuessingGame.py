import random
from art import logo


def game():
    print(logo)
    SECRET_NUMBER = random.randint(0, 100)
    LEVEL_BOOLEAN = False

    while not LEVEL_BOOLEAN:
        level = input("Type 'e' for easy mode, or 'h' for hard mode").lower()

        if level == 'e':
            lives = 10
            LEVEL_BOOLEAN = True
        elif level == 'h':
            lives = 5
            LEVEL_BOOLEAN = True
        else:
            print("Please pick between 'e' or 'h'. Other letters are not recognised")


    def ask_for_number(amount_of_lives):
        print(amount_of_lives)
        while amount_of_lives > 0:
            choice = int(input("Pick a number between 1 and 100: "))

            if choice == SECRET_NUMBER:
                return f"You did it! You found the random number: {SECRET_NUMBER}"
            elif choice > SECRET_NUMBER:
                print("Too high!")
                amount_of_lives -= 1
            elif choice < SECRET_NUMBER:
                print("Too low")
                amount_of_lives -= 1

            print(amount_of_lives)
        else:
            "You failed the game and lost!"


    final = ask_for_number(lives)
    print(final)
    play_again = input("Would you like to play again? 'y' or 'n' ")
    if play_again == 'y':
        game()
    else:
        print("Take care!")

game()
