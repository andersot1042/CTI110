# Trace Anderson
# 2/16/2026
# P1HW1
# This program performs exponent calculations and addition/subtraction using user input.

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("enter an integer as the exponent: "))
print()

result = base ** exponent

print(base, "raised to the power of", exponent, "is", result, "!!")
print()

print("-----Addition and Subtraction-----")
print()

start = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
subtract_num = int(input("Enter an integer to subtract: "))
print()

total = start + add_num - subtract_num

print(start, "+", add_num, "-", subtract_num, "is equal to", total)
