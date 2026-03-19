# Trace Anderson
# March 19 2026
# P3LAB - Money and change
# This program converts a dollar amount into the most efficient number of dollars, quarters, dimes, nickels and pennies (RIP)

# Get user input
amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents
cents = int(round(amount * 100))

# Handle no change case
if cents == 0:
    print("No change")
else:
    # Calculate each denomination
    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    # Output results (only if > 0)
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")
