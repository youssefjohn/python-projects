#
# def greet_with(name, location):
#     print(f"Your name is {name} and you live in {location}")
#
#
# greet_with('Youssef', 'London')
#
# greet_with(location='Wales', name='John')
#
#
# print(round((8 * 5) / 7))
#

# Write your code below this line 👇

# hi = "hello"
#
# for letter in hi:
#     print(letter)

# Write your code above this line 👆
newstring = ""
me = "hello 1 how are you"
for letter in me:
    if letter.isalpha():
        newstring += letter

print(newstring)
