from question import Question

class TrueFalseQuestion(Question):

    def render(self):
        print("\n" + self.prompt)
        print("1. True")
        print("2. False")

    def collect_answer(self):
        return input("Choose option: ")

    def grade(self, user_answer):
        if user_answer == "1":
            return self.answer.lower() == "true"

        elif user_answer == "2":
            return self.answer.lower() == "false"

        return False