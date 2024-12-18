import logging

logger = logging.getLogger(__name__)

class ApplicationEvents:
    def __init__(self, app):
        self.app = app
        self._register_events()

    def _register_events(self):
        @self.app.on_event("startup")
        async def startup_event():
            logger.info("** Starting the application.")
            logger.info("** Swagger Path: http://localhost:8000/docs")
        
        @self.app.on_event("shutdown")
        def shutdown_event():
            logger.info("** Shutting down the application.")
