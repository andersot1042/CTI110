# Trace Anderson
# March 4, 2026
# P2LAB2 - Keys and Values
# This program stores vehicle MPG values in a dictionary and calculates how many gallons of gas are needed for a specified trip.

vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
    "Tacoma": 25,
}

keys = vehicle_mpg.keys()
print(keys)

vehicle = input("Enter a vehicle to see its mpg: ")

print(f"The {vehicle} gets {vehicle_mpg[vehicle]} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons_needed = miles / vehicle_mpg[vehicle]

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
