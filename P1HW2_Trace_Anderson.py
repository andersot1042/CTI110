# Trace Anderson
# 2/16/2026
# P1HW2
# This program calculates and displays travel expenses

print("-----Travel Budget Calculator-----")
print()

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
accomodation = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))
print()

total_expenses = gas + accomodation + food
remaining_balance = budget - total_expenses

print("-----Travel Summary-----")
print("Destination:", destination)
print("Starting Budget: $", budget)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_balance)
