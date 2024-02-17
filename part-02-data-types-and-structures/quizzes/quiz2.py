import random
import json

quiz = [
    {
        "id": 1,
        "question": "How do you add a new element 'grapes' to the following list?\nfruits = ['apple', 'banana', 'cherry']",
        "options": [
            "fruits.add('grapes')",
            "fruits.append('grapes')",
            "fruits.insert('grapes')",
            "fruits.put('grapes')",
        ],
        "answer": 2,
    },
    {
        "id": 2,
        "question": "Which of the following is a valid tuple in Python?",
        "options": [
            "my_tuple = (1, 2, 3)",
            "my_tuple = tuple(1, 2, 3)",
            "my_tuple = [1, 2, 3]",
            "my_tuple = {1, 2, 3}",
        ],
        "answer": 1,
    },
    {
        "id": 3,
        "question": "What is the output of the following code?\ncolors = {'red', 'green', 'blue'}\nprint('green' in colors)",
        "options": ["True", "False", "1", "None"],
        "answer": 1,
    },
    {
        "id": 4,
        "question": "How do you access the value associated with the key 'age' in the following dictionary?\nperson = {'name': 'John', 'age': 30}",
        "options": ["person[1]", "person['age']", "person.age", "person.get('age')"],
        "answer": [2, 4],  # Note: Adjusted to list to indicate multiple correct answers
    },
    {
        "id": 5,
        "question": "Which method is used to add an element to a set in Python?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": 1,
    },
    {
        "id": 6,
        "question": "What will be the output of the following code?\nnumbers = [1, 2, 3, 4, 5]\nprint(numbers[-1])",
        "options": ["1", "5", "4", "Error"],
        "answer": 2,
    },
    {
        "id": 7,
        "question": "Which operation creates a new list containing all elements from both list1 and list2?\nlist1 = [1, 2, 3]\nlist2 = [4, 5, 6]",
        "options": [
            "list1 + list2",
            "list1.append(list2)",
            "list1.extend(list2)",
            "list1 && list2",
        ],
        "answer": 1,
    },
    {
        "id": 8,
        "question": "How do you remove 'banana' from the following set?\nfruits = {'apple', 'banana', 'cherry'}",
        "options": [
            "fruits.remove('banana')",
            "fruits.delete('banana')",
            "fruits.pop('banana')",
            "fruits.clear('banana')",
        ],
        "answer": 1,
    },
    {
        "id": 9,
        "question": "Which of the following creates a dictionary in Python?",
        "options": [
            "my_dict = {1: 'apple', 2: 'banana'}",
            "my_dict = [1: 'apple', 2: 'banana']",
            "my_dict = (1: 'apple', 2: 'banana')",
            "my_dict = {1, 'apple', 2, 'banana'}",
        ],
        "answer": 1,
    },
    {
        "id": 10,
        "question": "What is the result of trying to access a non-existent key 'color' in the following dictionary?\nperson = {'name': 'John', 'age': 30}",
        "options": ["30", "John", "KeyError", "None"],
        "answer": 3,
    },
]


def shuffle_quiz(quiz):
    # Function to shuffle questions and options
    random.shuffle(quiz)
    for q in quiz:
        random.shuffle(q["options"])
    return quiz


def load_answers(file_path):
    # Load answers from a separate file
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_quiz(questions, answers):
    # Run the quiz
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        user_answer = int(input("Your answer (1-4): ")) - 1
        correct_answer = answers[str(q["id"])]
        if isinstance(correct_answer, list):
            correct = user_answer + 1 in correct_answer
        else:
            correct = user_answer + 1 == correct_answer
        if correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your final score is {score}/{len(questions)}")


def main():
    answers = load_answers(
        "answers.json"
    )
    run_quiz(quiz, answers)

    # randomized_quiz = shuffle_quiz(quiz)
    # run_quiz(randomized_quiz)


if __name__ == "__main__":
    main()
