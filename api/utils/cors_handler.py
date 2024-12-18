from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class CORSHandler:
    def __init__(self, app: FastAPI, origins: list = ["http://localhost:3000"]):
        self.app = app
        self.origins = origins
        self._add_middleware()

    def _add_middleware(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
