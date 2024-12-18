from domain.interfaces.repositories import ILLMRepository
from openai import OpenAI

class OpenAIRepository(ILLMRepository):

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def _generate_response(self, messages: list) -> dict:
        response = self.client.chat.completions.create(
            messages=messages,
            model="gpt-4o-mini",
            #max_tokens=150 
        )
        return response.choices[0].message.content

    def analyzer_code(self, code: str, language: str) -> dict:
        explanation_message = {
            "role": "system", 
            "content": f"Hey! Can you explain what this code does in {language}, in simple terms? <pre>{code}</pre>"
        }

        refactor_message = {
            "role": "system",
            "content": f"Hey, can you improve this code and just send me the updated version? <pre>{code}</pre> in {language}"
        }


        explanation_refactor_message = {
            "role": "system",
            "content": f"Hey, can you walk me through what you changed in the refactor, step by step in {language}? I'd love to understand what you were thinking while making those changes. Feel free to explain it like you're explaining it to a friend. Don't use markdown."
        }

        explanation = self._generate_response([explanation_message])
        refactored_code = self._generate_response([refactor_message])
        explanation_of_refactor = self._generate_response([explanation_refactor_message])
        
        return {
            "explanation": explanation.strip(),
            "refactored_code": refactored_code.strip(),
            "explanation_of_refactor": explanation_of_refactor.strip()
        }
