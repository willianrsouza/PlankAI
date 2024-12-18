from abc import ABC, abstractmethod

class ILLMRepository(ABC):
    
    @abstractmethod
    def analyzer_code(self, code: str, language: str) -> dict:
        """
        Explains the code, suggests a refactor, and explains the reasoning behind the refactor.

        :param code: The source code to be explained and refactored.
        :param language: The natural language in which the code explanation should be provided.
        :return: A dictionary with three keys: 'explanation', 'refactored_code', and 'explanation_of_refactor'.
        """
        pass
    