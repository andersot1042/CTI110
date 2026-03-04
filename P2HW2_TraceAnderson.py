# Trace Anderson
# March 4, 2026
# P2HW2 - Grade list
# This program collects module grades and calculates the highest, lowest, sum and average of those grades.

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

low_grade = min(module_grades)
high_grade = max(module_grades)
sum_grades = sum(module_grades)
avg_grade = sum_grades / len(module_grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<18} {low_grade}")
print(f"{'Highest Grade:':<18} {high_grade}")
print(f"{'Sum of Grades:':<18} {sum_grades}")
print(f"{'Average:':<18} {avg_grade:.2f}")
print("-" * 31)
