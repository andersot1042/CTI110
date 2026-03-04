# Trace Anderson
# March 4, 2026
# P2HW1 - Travel Budget Calculator
# This program calculates and displays travel expenses.

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
dest = input("Enter your travel destination: ")
gas = float(input("How much do you you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel?" ))
food = float(input("Last, how much do you need for food? "))

expenses = gas + hotel + food 
remaining = budget - expenses

print("\n------------Travel Expenses------------")

print(f"{'Location:':<20} {dest}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accomodation:':<20} ${hotel:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")

print("-" * 39)
print()
print(f"{'Remaining Balance:':<20} ${remaining:,.2f}")

