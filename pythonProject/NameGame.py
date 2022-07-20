


def details():
    count = 1
    while count:
        try:
            name = str(input("What is your name: ")).lower()
            age = int(input("How old are you: "))
        except ValueError:
            print("Wrong value")
            continue

        count -= 1
        details = [name, age]

    return details



def person():
    list_of_bad_people = ['albert', 'john', 'gareth']


    new_person = details()
    first_name = new_person[0]
    age = new_person[1]

    for name in list_of_bad_people:
        if first_name == name:
            print("You are a criminal!")
        else:
            pass
    print(f"{first_name}, {age}")


person()







