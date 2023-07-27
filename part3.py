import requests
import random

url= "https://opentdb.com/api.php?amount=3&category=15&difficulty=easy&type=multiple"


data= requests.get(url).json()

for i in data["results"]:
    print(i["question"])
    new_answers= []
    new_answers.append(i["correct_answer"])
    for x in i["incorrect_answers"]:
        new_answers.append(x)
      
    # METHOD 1
       # add .sort() method onto our list of answers
    new_answers.sort()
    print(new_answers)

    # METHOD 2
    random.shuffle(new_answers)
    print(new_answers)
