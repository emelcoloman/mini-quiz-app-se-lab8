class Quiz:
    def __init__(self, questions, grading_strategy):
        self.questions = questions
        self.grading_strategy = grading_strategy

    def start(self):
        score = 0

        for question in self.questions:
            is_correct = question.execute()

            if is_correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        self.grading_strategy.calculate(score, len(self.questions))