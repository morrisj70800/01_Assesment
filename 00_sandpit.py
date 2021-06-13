import csv
import random

with open('q_and_a_csv.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)

valid_questions = []

for item in data:
    if item[0] != "ignore_me":
        valid_questions.append(item)

print(valid_questions)

for item in range(0, 10):

    print()
    question_ans = random.choice(valid_questions)
    question = question_ans[0]
    answer= question_ans[1]

    print("question:", question)
    print("right answer", answer)

    answer_options = [answer]

    for option in range(0,3):
        # choose answer
        wrong_ans = random.choice(data)
        wrong = wrong_ans[1]
        answer_options.append(wrong)

    print("Answer Options", answer_options)
    print()