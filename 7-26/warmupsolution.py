#!/usr/bin/env python3
import requests
import html
import random
import string

"""Solution to the 7-26 Morning Exercise | 100% of code written by ChatGPT!"""

# Dictionary of categories with their corresponding IDs
categories = {
    "9": "General Knowledge",
    "10": "Entertainment: Books",
    "11": "Entertainment: Film",
    "12": "Entertainment: Music",
    "13": "Entertainment: Musicals & Theatres",
    "14": "Entertainment: Television",
    "15": "Entertainment: Video Games",
    "16": "Entertainment: Board Games",
    "17": "Science & Nature",
    "18": "Science: Computers",
    "19": "Science: Mathematics",
    "20": "Mythology",
    "21": "Sports",
    "22": "Geography",
    "23": "History",
    "24": "Politics",
    "25": "Art",
    "26": "Celebrities",
    "27": "Animals",
    "28": "Vehicles",
    "29": "Entertainment: Comics",
    "30": "Science: Gadgets",
    "31": "Entertainment: Japanese Anime & Manga",
    "32": "Entertainment: Cartoon & Animations"
}

print("Trivia Categories Menu:\n")
for number, category in categories.items():
    print(f"{number}: {category}")

while True:
    user_choice = input("Enter the number of the category you want: ")
    if user_choice in categories:
        selected_category = categories[user_choice]
        break
    print("Invalid choice. Please enter a number from the menu.")

while True:
    num_questions = input("Enter the number of questions you want to receive: ")
    if num_questions.isdigit() and int(num_questions) > 0:
        break
    print("Invalid input. Please enter a positive number.")

url = f"https://opentdb.com/api.php?amount={num_questions}&category={user_choice}"

print(f"\nYou selected category: {selected_category}")
print(f"You will receive {num_questions} question(s) from this category.")
print(f"Generated URL: {url}")

# Make the API request using the requests library
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    questions = data["results"]
    print("\nHere are your questions:\n")

    # Initialize score variables
    correct_answers = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, 1):
        question_text = html.unescape(question['question'])
        print(f"{i}. {question_text}")

        # Randomize the order of answers
        answers = [html.unescape(answer) for answer in question['incorrect_answers']] + [html.unescape(question['correct_answer'])]
        random.shuffle(answers)

        # Display answers as A, B, C, D
        for j, answer in enumerate(answers):
            print(f"{string.ascii_uppercase[j]}. {answer}")

        # Let the user choose which answer they think is correct
        while True:
            try:
                user_answer = input("Enter the letter of the correct answer: ").upper()
                if user_answer in string.ascii_uppercase[:len(answers)]:
                    break
                else:
                    print("Invalid choice. Please enter a letter from the options.")
            except ValueError:
                print("Invalid input. Please enter a letter.")

        # Check if the user's answer is correct
        correct_answer_index = answers.index(html.unescape(question['correct_answer']))
        correct_answer = string.ascii_uppercase[correct_answer_index]
        if user_answer == correct_answer:
            print("Correct answer!\n")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.\n")

    # Print the final score
    print(f"You got {correct_answers} out of {total_questions} questions correct!")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

