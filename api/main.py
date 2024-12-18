import uvicorn
import logging
from dotenv import load_dotenv
import os

from fastapi import FastAPI, HTTPException, Depends
from utils.events import ApplicationEvents
from utils.cors_handler import CORSHandler 
from application.use_cases.code_snippet_analyzer import CodeSnippetAnalyzerUseCase
from application.schemas.code_snippet_input import CodeSnippetInput
from adapters.external.repositories.openai import OpenAIRepository
from infrastructure.logging.logging_config import setup_logging

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI(title="PlankAI - Generative Code Analyzer (API)", version="1.0.0")
        CORSHandler(self.app) 
        ApplicationEvents(self.app)
        self._add_endpoints()

    def _add_endpoints(self):
        @self.app.post("/code-snippet-analyzer", summary="Explain and suggest refactor for code")
        def analyze_code_snippet(input: CodeSnippetInput):
            try:
                api_key = os.getenv("API_KEY")
                
                if not api_key:
                    raise ValueError("API_KEY not found in environment variables")

                openai_repository = OpenAIRepository(api_key=api_key)
                use_case = CodeSnippetAnalyzerUseCase(openai_repository)
                
                return use_case.execute(input)
            except Exception as e:
                logger.error(f"Error while processing the code: {e}", exc_info=True)
                raise HTTPException(status_code=500, detail="An error occurred during processing.")

app = FastAPIApp().app 

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
