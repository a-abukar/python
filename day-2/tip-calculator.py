
print("Welcome to the tip calculator!")
# Converts user input into a decimal number
bill = float(input("What was the total bill? £"))
# Converts the user input into an integer
tip = int(input("How much tip would you like to give? Pick from one of, 5, 10, 15, 20: "))
people = int(input("How many people to split the bill? "))
# User inputs above are taken as integers and can be used to calculate directly
bill_per_person = (bill + (bill*(tip/100))) / people
# Round function, rounds to desired number of decimal places if they are available
final_amount = round(bill_per_person, 2)
# Function to always have 2 decimal places when money is involved
final_amount = "{:.2f}".format(bill_per_person)

# Prints the desired result (how much each person pay)
print(f"Each person should pay {final_amount}")