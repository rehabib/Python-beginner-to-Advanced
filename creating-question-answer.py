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

# Main function to collect questions from the user
def get_questions():
    quiz = []
    while True:
        q_type = input("\nEnter question type (multiple_choice / true_false / open_ended): ").strip().lower()
        question = input("Enter the question: ")

        if q_type == "multiple_choice":
            print("Enter 4 options (Example: A. Option1)")
            options = []
            for i in range(4):
                opt = input(f"Option {i+1}: ")
                options.append(opt)
            answer = input("Enter the correct option letter (A/B/C/D): ").strip().upper()
            quiz.append({"type": q_type, "question": question, "options": tuple(options), "answer": answer})

        elif q_type == "true_false":
            answer = input("Enter the correct answer (True/False): ").strip().capitalize()
            quiz.append({"type": q_type, "question": question, "answer": answer})

        elif q_type == "open_ended":
            answer = input("Enter the correct answer: ").strip()
            quiz.append({"type": q_type, "question": question, "answer": answer})

        else:
            print("❌ Invalid question type. Try again.")
            continue

        more = input("Do you want to add another question? (yes/no): ").strip().lower()
        if more != "yes":
            break
    return quiz

# Function to run the quiz
def run_quiz(quiz_data):
    score = 0
    total_questions = 0
    correct_answers = 0
    incorrect_answers = 0

    for i, q in enumerate(quiz_data, 1):
        print(f"\nQuestion {i}:")
        is_correct = False

        if q["type"] == "multiple_choice":
            is_correct = handle_multiple_choice(q)
        elif q["type"] == "true_false":
            is_correct = handle_true_false(q)
        elif q["type"] == "open_ended":
            is_correct = handle_open_ended(q)

        if is_correct:
            print("✅ Correct!")
            score += 1
            correct_answers += 1
        else:
            print(f"❌ Incorrect. The correct answer is: {q['answer']}")
            incorrect_answers += 1

        total_questions += 1

        cont = input("Do you want to continue the quiz? (yes/no): ").strip().lower()
        if cont != "yes":
            break

    print("\n📊 Quiz Summary:")
    print(f"Total questions answered: {total_questions}")
    print(f"Correct answers: {correct_answers}")
    print(f"Incorrect answers: {incorrect_answers}")
    print(f"Final score: {score}/{total_questions}")

# Run the full quiz system
questions = get_questions()
run_quiz(questions)