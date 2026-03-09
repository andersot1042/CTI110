# Trace Anderson
# March 9, 2026
# P3HW2 - pay stub calculator
# A program to calculate regular pay, overtime pay, and gross pay based on hours worked.

"""
Pseudocode:
1.  Get input for employee's name (string).
2.  Get input for hours worked (float).
3.  Get input for pay rate (float).
4.  Check if hours worked are greater than 40:
    a. If yes:
       - Overtime hours = hours worked - 40
       - Overtime pay = Overtime hours * (pay rate * 1.5)
       - Regular pay = 40 * pay rate
    b. If no (else):
       - Overtime hours = 0
       - Overtime pay = 0
       - Regular pay = hours worked * pay rate
5.  Calculate gross pay = Regular pay + Overtime pay.
6.  Display results in a formatted table as shown in the reference image.
"""

# Get user input
emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime and pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    reg_hour_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    reg_hour_pay = hours_worked * pay_rate

gross_pay = reg_hour_pay + overtime_pay

# Display results
print("-" * 40)
print(f"Employee name:    {emp_name}")
print()
# Headers
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("-" * 85)
# Data Row
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<15.2f}${reg_hour_pay:<14.2f}${gross_pay:<15.2f}")