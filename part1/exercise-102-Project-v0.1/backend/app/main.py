import os
import logging

from fastapi import FastAPI

app = FastAPI()

PORT = os.environ.get('PORT', "NNNN")
logger = logging.getLogger("uvicorn.error")
logger.info(f"Server started in port {PORT}")

@app.get("/")
async def root():
    return {"message": "Hello World"}