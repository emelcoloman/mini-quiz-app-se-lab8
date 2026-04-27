from multiple_choice import MultipleChoiceQuestion
from true_false import TrueFalseQuestion
from short_answer import ShortAnswerQuestion

class QuestionFactory:

    @staticmethod
    def create_question(data):
        question_type = data["type"]

        if question_type == "multiple_choice":
            return MultipleChoiceQuestion(
                data["prompt"],
                data["options"],
                data["answer"]
            )

        elif question_type == "true_false":
            return TrueFalseQuestion(
                data["prompt"],
                data["answer"]
            )

        elif question_type == "short_answer":
            return ShortAnswerQuestion(
                data["prompt"],
                data["answer"]
            )

        raise ValueError("Unknown question type")