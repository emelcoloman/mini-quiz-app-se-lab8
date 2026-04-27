from abc import ABC, abstractmethod

class GradingStrategy(ABC):

    @abstractmethod
    def calculate(self, score, total):
        pass