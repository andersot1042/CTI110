# Trace Anderson
# 03/30/2026
# P4HW1 
# This program collects a user-defined number of scores, validates input, removes the lowest score, calculates the average and assigns a letter grade.

# ----------- Pseudocode -----------
# 1. Ask user how many scores they want to enter
# 2. Create an empty list to store scores
# 3. Loop for the number of scores:
#     a. Ask for a score
#     b. While score is invalid (<0 or >100):
#           - Display error message
#           - Ask again for the same score number
#     c. Add valid score to list
# 4. Find the lowest score
# 5. Remove lowest score from list
# 6. Calculate average of remaining scores
# 7. Determine letter grade based on average
# 8. Display results

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))

    scores.append(score)

lowest_score = min(scores)

scores.remove(lowest_score)

average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >=80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")

