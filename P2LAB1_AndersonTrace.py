# Trace Anderson
# March 4, 2026
# P2LAB1 - Circle Calculations
# A program that calculates diameter, circumference and area based on radius.

import math # We need this to get a precise value for Pi

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate values
diameter = 2 * radius
circumference = 2 * math.pi * radius 
area = math.pi * (radius ** 2)

# Display results with required formatting
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")