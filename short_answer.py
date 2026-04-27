from question import Question

class ShortAnswerQuestion(Question):

    def render(self):
        print("\n" + self.prompt)

    def collect_answer(self):
        return input("Your answer: ")

    def grade(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()