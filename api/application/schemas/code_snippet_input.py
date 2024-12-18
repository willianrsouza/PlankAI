from enum import Enum
from pydantic import BaseModel, Field

class LanguageEnum(Enum):
    """Supported languages for the code explanation"""
    PORTUGUESE = "Portuguese"
    ENGLISH = "English"
    SPANISH = "Spanish"
    FRENCH = "French"

class ModelEnum(Enum):
    """Supported models for code analysis and refactoring"""
    GPT = "GPT"
    GEMINI = "Gemini"

class CodeSnippetInput(BaseModel):
    code: str = Field(..., title="Code to analyze", description="The source code snippet to analyze and explain")
    language: LanguageEnum = Field(
        ...,
        title="Explanation Language",
        description="The language in which the code explanation will be provided. Choose from English, Portuguese, etc.",
    )
    model: ModelEnum = Field(
        "GPT", 
        title="Model to use", 
        description="The LLM model to use for analyzing and explaining the code, such as 'GPT' or 'Gemini'.",
    )

    class Config:
        schema_extra = {
            "example": {
                "code": "def add(a, b): return a + b",
                "language": "English",
                "model": "GPT"
            }
        }
