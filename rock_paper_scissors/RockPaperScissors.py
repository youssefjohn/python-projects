import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input("Please pick a number between 0-2, 0 is rock, 1 is paper and 2 is scissors\n>"))

computers_choice = random.randint(0, 2)

choices = []
choices.extend([rock, paper, scissors])

users_outcome = choices[user_input]
computers_outcome = choices[computers_choice]

#Rock vs all
if users_outcome == choices[0] and computers_outcome == choices[1]:
    print("Computer wins! Paper beats rock!")
elif users_outcome == choices[1] and computers_outcome == choices[0]:
    print("You win! Paper beats rock!")
elif users_outcome == choices[0] and computers_outcome == choices[2]:
    print("You win! Rock beats scissors!")
elif users_outcome == choices[2] and computers_outcome == choices[0]:
    print("Computer wins! Rock beats scissors!")
elif users_outcome == choices[1] and computers_outcome == choices[2]:
    print("Computer wins! scissors beat paper!")
elif users_outcome == choices[2] and computers_outcome == choices[1]:
    print("You win! scissors beat paper!")
elif users_outcome == choices[2] and computers_outcome == choices[2]:
    print("Draw!")
elif users_outcome == choices[1] and computers_outcome == choices[1]:
    print("Draw!")
elif users_outcome == choices[0] and computers_outcome == choices[0]:
    print("Draw!")



print(users_outcome)
print(computers_outcome)


