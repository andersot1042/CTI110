# Trace Anderson
# 4/16/26
# P4LAB2 - Multiplication table

run_again = "yes"

while run_again.lower() == "yes":

    num = int(input("Enter an integer: "))

    if num < 0:
        print("This program does not handle negative numbers.")

    else:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")

    run_again = input("\nWould you like ro tun the program again? ")

print("Exiting program...")



