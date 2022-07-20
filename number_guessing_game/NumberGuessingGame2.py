import random

EASY = 10
HARD = 5

def set_difficulty():
    choice = input("Easy 'e' or Hard 'h': ").lower()
    if choice == 'e':
        return EASY
    else:
        return HARD


def check_choice(answer, turns):
    while turns > 0:

        guess = int(input("Pick a number between 1 and 100: "))

        if guess == answer:
            return f"You did it! You found the random number: {answer}"
        elif guess > answer:
            print("Too high!")
            turns -= 1
        elif guess < answer:
            print("Too low")
            turns -= 1
        print(f"{turns} lives remaining.")



def game():
    print("Welcome to the number guessing game")
    secret_number = random.randint(0, 100)
    difficulty = set_difficulty()
    print(f"You have {difficulty} lives to start with.")
    result = check_choice(secret_number, difficulty)
    print(result)



game()
