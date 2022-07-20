
class Parent:

    blueEyes = 'Yes'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tactic(self, power):
        return f"{self.name} uses {power} against opponent!"


class Child(Parent):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def response(self, power):
        return f"{self.name} uses child {power} against child opponent"

john = Parent('john', 31)

baby = Child('haythem', 1)

print(john.name)
print(baby.name)
print(baby.blueEyes)
print(baby.tactic('Screech'))



