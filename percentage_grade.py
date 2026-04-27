from grading_strategy import GradingStrategy

class PercentageGrade(GradingStrategy):

    def calculate(self, score, total):
        percentage = (score / total) * 100

        print(f"\nFinal Score: {score}/{total}")
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 60:
            print("Result: Pass")
        else:
            print("Result: Fail")

        return percentage