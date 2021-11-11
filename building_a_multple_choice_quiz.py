
# import the Question class from the question.py file
#    to allow us to create our own data type of Question
from question import Question

question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n",
]

# create a list of three objects of the Question class
# NOTE: an object is an instance of a class (class is a template)
#     and the object has three actual questions with actual information - questions
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)
