

class Employee:

    company = "Foundry"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sayDetails(self):
        print(f"{self.name}")

    def hobby(self, hob):
        return f"I love doing {hob}"


a = Employee('youssef', 31, 'male')

print(a.hobby("boxing"))

