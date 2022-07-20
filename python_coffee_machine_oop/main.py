from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

customer_drink = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

offer_drink = True

while offer_drink:
    choice = input("What would you like? ").lower()
    if choice == 'find':
        print(customer_drink.get_items())
        continue
    elif choice == 'off':
        offer_drink = False
        continue
    elif choice == 'report':
        machine.report()
        money_machine.report()
        continue
    else:
        # Assign the drink to a variable
        drink = customer_drink.find_drink(choice)
        print(f"You have chosen: {choice}")

    # Check resources using the chosen drink
    ## Then check if customer can offord
    if machine.is_resource_sufficient(drink):
        money_machine.make_payment(drink.cost)
        machine.make_coffee(drink)

    else:
        # If there are not enough resources for the drink, tap into the Methods if statement
        machine.is_resource_sufficient(drink)




















