import random
import hangman_words
from replit import clear
from os import system, name
from hangman_art import *


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)

chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


length_of_chosen_word = len(chosen_word)
display = []
for _ in range(length_of_chosen_word):
    display.append('_')

lives = 6
end_of_game = False
while not end_of_game:
    # Take a users guess
    guess = input("Guess a letter: ").lower()
    clear()

    # If the user has already guessed a correct letter, then warn them they cant use it again
    if guess in display:
        print("You have already used that letter before!")


    # Check each position of the chosen word, against the guess
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess



    # If the guess isn't in the chosen word, decrease the lives by 1. If lives are 0, end the game, User loses.
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter '{guess}', is not in the chosen word, you lose a life! Lives remaining: {lives}")
        if lives == 0:
            print("You Lose!")
            end_of_game = True


    # If their are no more blanks left in the chosen word and it is fully revealed, Users wins.
    if '_' not in display:
        print("You win!")
        end_of_game = True


    # Print out Ascii and chosen word(partially hidden with blanks)

    print(stages[lives])
    final_display = ''.join(display)
    print(''.join(display))


