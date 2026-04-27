import json

from question_factory import QuestionFactory
from quiz import Quiz
from percentage_grade import PercentageGrade

with open("questions.json", "r") as file:
    question_data = json.load(file)

questions = []

for data in question_data:
    question = QuestionFactory.create_question(data)
    questions.append(question)

grading_strategy = PercentageGrade()

quiz = Quiz(questions, grading_strategy)
quiz.start()