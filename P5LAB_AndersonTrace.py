# Trace Anderson
# April 28 2026
# P5LAB - Self Checkout Simulator
# This program simulates a self-checkout machine. It generates a random total, accepts user payment, calculates change, and displays the breakdown of coins.

import random

# Disperse change into denominations
def disperse_change(change):
    change = int(round(change * 100))

    dollars = change // 100
    change %= 100

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print("\nChange is:")

    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars != 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters != 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes != 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels != 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies != 1 else 'y'}")

# Main function
def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # User input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - total_owed, 2)

    print(f"Change is: ${change:.2f}")

    # Call function
    disperse_change(change)

# Call main
main()