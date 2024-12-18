from domain.interfaces.repositories import ILLMRepository
from application.schemas.code_snippet_input import CodeSnippetInput
from application.validators.code_snippet_validator import CodeSnippetValidator, ValidationException

class CodeSnippetAnalyzerUseCase:
    def __init__(self, repository: ILLMRepository):
        self.repository = repository

    def execute(self, input: CodeSnippetInput):
        try:
            CodeSnippetValidator.validate(input)
        except ValidationException as e:
            return e.to_dict()

        return self.repository.analyzer_code(input.code, input.language)
