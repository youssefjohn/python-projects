# Tip Calculator
print("Welcome to the tip calculator.")
# Askf or the bill and convert into a float
bill = input("What was the total bill? ")
bill = float(bill)

#Ask for the tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate the bill and tip together
total_and_tip = bill + bill * (tip / 100)

# Find the number of people splitting
num_of_people = int(input("How many people to split the bill? "))

# Find the price per person
per_person_cost = total_and_tip/num_of_people

# Print the final cost per person, rounded to the nearest .00 decimal point
print(round(per_person_cost, 2))
print("{:.2f}".format(per_person_cost))
