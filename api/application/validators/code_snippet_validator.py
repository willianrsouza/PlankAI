class CodeSnippetValidator:
    @staticmethod
    def validate(input):
        errors = {}

        if not input.code:
            errors["code"] = "The 'code' field is required and must be a valid string."

        if not input.language:
            errors["language"] = "The 'language' field is required and must be a valid string."

        if not input.model:
            errors["model"] = "The 'model' field is required and must be a valid string."

        if errors:
            raise ValidationException(errors)

class ValidationException(Exception):
    def __init__(self, errors):
        super().__init__("Erro de validação")
        self.errors = errors

    def to_dict(self):
        return {"errors": self.errors}
