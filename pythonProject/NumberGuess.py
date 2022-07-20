import random



print("This is your chance to guess a number. Please try your best :) \n"
      "You may get it right!")

randomNum = random.randint(1, 10)



def Question():
      counter = 0
      while counter < 4:
            question = int(input("Pick a number: "))
            counter += 1
            if question == randomNum:
                  print(f"Great! your number matched!!")
                  break
            elif question > randomNum:
                  print(f"Too high")
                  continue
            elif question < randomNum:
                  print("Too low")
                  continue
            else:
                  print(f"Sorry {question} is not right")

      else:
          print("Guesses exceeded!")


Question()