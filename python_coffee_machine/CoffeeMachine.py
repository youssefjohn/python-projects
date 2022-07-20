from menu import MENU, resources


QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01


def check_resources_sufficient(resources_dict, user_choice):
    """Returns True if there is enough resources, returns False if there is not"""
    for key in user_choice:
        if user_choice[key] >= resources_dict[key]:
            return f"Sorry there is not enough {key}"
    return True


def make_drink(resources_dict, user_choice):
    """Deducts the value of the drink, from the resources"""
    for key in user_choice:
        resources_dict[key] -= user_choice[key]
    return True


def process_coins():
    """Calculates number of coins against value of coins"""
    calculation = int(input("Quarter: ")) * 0.25
    calculation += int(input("Dime: ")) * 0.10
    calculation += int(input("Nickle: ")) * 0.05
    calculation += int(input("Pennie: ")) * 0.01
    return calculation


def make_transaction(user_money, cost_of_drink):
    """Returns True if payment is accepted, returns False if payment is declined"""
    if user_money >= cost_of_drink:
        return True
    else:
        return False


def game():
    coffee_on = True
    offer_drink = True

    while coffee_on:
        while offer_drink:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == 'off':
                coffee_on = False
                break
            elif choice == 'report':
                for item in resources:
                    print(f"{item}: {resources[item]}")
            elif choice in MENU.keys():
                name_of_choice = choice
                cost_of_choice = MENU[choice]['cost']
                choice = MENU[choice]["ingredients"]
                break
            elif choice != 'latte' or choice != 'cappuccino' or choice != 'espresso':
                print("Please pick from the menu. There are only 3 choices")

        if not coffee_on:
            break

        checking_resources = check_resources_sufficient(resources, choice)

        if checking_resources:
            print(f"The cost of a {name_of_choice} is: {cost_of_choice}")
            users_money = process_coins()
            payment = make_transaction(users_money, cost_of_choice)
            if payment:
                make_drink(resources, choice)
                print(f"Here is your {name_of_choice}")
                coffee_on = False
            else:
                print("Not enough money")


game()
