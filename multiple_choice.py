from question import Question

class MultipleChoiceQuestion(Question):
    def __init__(self, prompt, options, answer):
        super().__init__(prompt, answer)
        self.options = options

    def render(self):
        print("\n" + self.prompt)

        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def collect_answer(self):
        return input("Choose option number: ")

    def grade(self, user_answer):
        try:
            selected = self.options[int(user_answer) - 1]
            return selected.lower() == self.answer.lower()
        except:
            return False