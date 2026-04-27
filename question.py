from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def execute(self):
        self.render()
        user_answer = self.collect_answer()
        return self.grade(user_answer)

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def collect_answer(self):
        pass

    @abstractmethod
    def grade(self, user_answer):
        pass