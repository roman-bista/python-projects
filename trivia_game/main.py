import random

questions = {
    "what is the keyword to define a fn?": "def",
    "what datatype is used to store True and False?": "bool",
    "which symbol is used to comment in python?": "#",
    "which keyword is used for loop in python?": "for",
    "which keyword is used for conditional statement?": "if",
    "which function is used to display output?": "print",
    "which function is used to take user input?": "input",
    "what datatype stores whole numbers?": "int",
    "what datatype stores decimal numbers?": "float",
    "what datatype stores text?": "str",
    "which keyword is used to create a class?": "class",
    "which keyword is used to import modules?": "import",
    "which datatype is immutable list or tuple?": "tuple",
    "which keyword is used to handle exceptions?": "try",
    "which keyword is used with try block?": "except",
    "which loop runs until condition becomes false?": "while",
    "which operator is used for equality check?": "==",
    "which keyword is used to return value from function?": "return"
}

def python_trivia_game():

    print("\n===== PYTHON TRIVIA GAME =====")

    questions_list = list(questions.keys())

    total_qsn = 5
    score = 0

    selected_qsn = random.sample(questions_list, total_qsn)

    for idx, question in enumerate(selected_qsn, start=1):

        print(f"\nQuestion {idx}/{total_qsn}")
        print(question)

        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {correct_answer}")

    percentage = (score / total_qsn) * 100

    print("\n===== RESULT =====")
    print(f"Score: {score}/{total_qsn}")
    print(f"Percentage: {percentage}%")

    if percentage == 100:
        print("Excellent! Python master!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing Python!")

while True:

    python_trivia_game()

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\nThanks for playing!")
        break