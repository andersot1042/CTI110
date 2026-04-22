# Lord of the Rings Multiple Choice Quiz Game

def ask_question(question, options, correct_answer):
    print(question)
    for key, value in options.items():
        print(f"  {key}) {value}")
    
    user_answer = input("> ").strip().upper()

    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print("Incorrect!\n")
        return 0


def main():
    print("Welcome to the Lord of the Rings Quiz!\n")

    score = 0

    questions = [
        {
            "question": "Who is the ring-bearer?",
            "options": {"A": "Sam", "B": "Frodo", "C": "Bilbo", "D": "Merry"},
            "answer": "B"
        },
        {
            "question": "What is the name of Gandalf's horse?",
            "options": {"A": "Shadowfax", "B": "Brego", "C": "Arod", "D": "Hasufel"},
            "answer": "A"
        },
        {
            "question": "What is Smeagol's alter ego?",
            "options": {"A": "Drogo", "B": "Ugluk", "C": "Gollum", "D": "Deagol"},
            "answer": "C"
        },
        {
            "question": "What is the name of Aragorn's sword?",
            "options": {"A": "Narsil", "B": "Orcrist", "C": "Glamdring", "D": "Anduril"},
            "answer": "D"
        },
        {
            "question": "How many Istari are there?",
            "options": {"A": "Seven", "B": "Two", "C": "Five", "D": "Three"},
            "answer": "C"
        },
        {
            "question": "Who is the dark lord that forged the One Ring?",
            "options": {"A": "Saruman", "B": "Sauron", "C": "Witch-king", "D": "Denethor"},
            "answer": "B"
        },
        {
            "question": "Who was the Dark Lord that Sauron served in the First Age?",
            "options": {"A": "Ungolient", "B": "Ancalagon the Black", "C": "Morgoth", "D": "Glorfindel"},
            "answer": "C"
        },
        {
            "question": "How many golden hairs from atop her head did Lady Galadriel gift Gimli the dwarf before the Fellowship departed Lothlorien?",
            "options": {"A": "None. She would never give her hair to a dwarf.", "B": "1", "C": "3", "D": "10"},
            "answer": "C"
        },
        {
            "question": "Which mountain was the One Ring forged in?",
            "options": {"A": "Lonely Mountain", "B": "Mount Doom", "C": "Misty Mountain", "D": "Mount Gundabad"},
            "answer": "B"
        },
        {
            "question": "How many consecutive terms did Samwise serve as mayor of the Shire?",
            "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
            "answer": "C"
        }
    ]

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])

    print("Quiz Complete!")
    print(f"You got {score} out of {len(questions)} correct.\n")

    # Character classification
    if score <= 3:
        character = "Gollum – Lost and confused, but still hanging in there."
    elif score <= 5:
        character = "Pippin – Curious, learning, and occasionally clueless."
    elif score <= 7:
        character = "Samwise Gamgee – Loyal, dependable, and strong-hearted."
    elif score <= 9:
        character = "Aragorn – Knowledgeable, skilled, and a true leader."
    else:
        character = "Gandalf – Wise beyond measure. A true master of Middle-earth!"

    print("Character Analysis:")
    print(character)
    print(f"(Score: {score}/{len(questions)})")

if __name__ == "__main__":
    main()