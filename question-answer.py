#dictionary, loop, conditional, function, list
# This program will ask the user a question and check if the answer is correct.
# If the answer is correct, it will print a message and ask if the user wants to continue.
# If the answer is incorrect, it will print a message and ask if the user wants to continue.
# The program will continue until the user chooses to stop.
# The program will also keep track of the number of correct and incorrect answers.
# The program will also keep track of the number of questions asked.
# The program will also keep track of the number of correct and incorrect answers.
# The program will also keep track of the number of questions asked.
# The program will also keep track of the number of correct and incorrect answers.
''' Loop  to go through multiple questions.

List  to store the questions (or keys from the dictionary).

Dictionary  to store question-answer pairs.

Function  to ask the question and check the answer. '''

# Quiz Questions
quiz = [
    {
        "type": "multiple_choice",
        "question": "What is the capital of Ethiopia?",
        "options": ("A. Addis Ababa", "B. Mekelle", "C. Gondar", "D. Dire Dawa"),
        "answer": "A"
    },
    {
        "type": "true_false",
        "question": "Python is a type of snake and a programming language.",
        "answer": "True"
    },
    {
        "type": "open_ended",
        "question": "Who is the founder of Microsoft?",
        "answer": "Bill Gates"
    }
]

# Function to handle multiple choice
def handle_multiple_choice(q):
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    return user_answer == q["answer"]

# Function to handle true/false
def handle_true_false(q):
    print(q["question"])
    user_answer = input("Your answer (True/False): ").strip().capitalize()
    return user_answer == q["answer"]

# Function to handle open-ended
def handle_open_ended(q):
    print(q["question"])
    user_answer = input("Your answer: ").strip().lower()
    return user_answer == q["answer"].lower()

# Main quiz function
def run_quiz(quiz_data):
    score = 0
    for i, q in enumerate(quiz_data, 1):
        print(f"\nQuestion {i}:")
        if q["type"] == "multiple_choice":
            if handle_multiple_choice(q):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is {q['answer']}")
        elif q["type"] == "true_false":
            if handle_true_false(q):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is {q['answer']}")
        elif q["type"] == "open_ended":
            if handle_open_ended(q):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is {q['answer']}")
    print(f"\nYour final score is: {score}/{len(quiz_data)}")

# Run the quiz
run_quiz(quiz)
