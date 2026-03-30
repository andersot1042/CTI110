# Trace Anderson
# 03/30/2026
# P4HW2
# This program calculates gross pay for multiple employees, including overtime and displays totals at the end.

#------------ Pseudocode ------------
# 1. Initialize totals for overtime, regular pay, gross pay, and employee count
# 2. Ask for employee name
# 3. While name is not "Done":
#    a. Ask for hours worked and pay rate
#    b. Calculate overtime hours and pay
#    c. Calculate regular pay and gross pay
#    d. Add values to totals
#    e. Display formatted employee table
#    f. Ask for next employee name
# 4. When "Done" is entered, display totals



total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

name = input('Enter employee\'s name or "Done" to terminate: ')

while name != "Done":

    hours = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    # Overtime calculation
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    employee_count += 1

    # Display formatted output
    print("\nEmployee name: ", name)
    print()
    print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay")
    print("-----------------------------------------------------------------------------")

    print(f"{hours:.1f}          {pay_rate:.2f}      {overtime_hours:.1f}        "
          f"{overtime_pay:.2f}         ${regular_pay:.2f}      ${gross_pay:.2f}")
    
    name = input('Enter employee\'s name or "Done" to terminate: ')

# Final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")