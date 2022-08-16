import os
import logging
import uuid
from datetime import datetime

from fastapi import FastAPI

# Create an app:
app = FastAPI()

# Log the port of the server:
PORT = os.environ.get('PORT', "NNNN")
logger = logging.getLogger("uvicorn.error")
logger.info(f"Server started in port {PORT}")

# Store a random string:
random_string = uuid.uuid1()

@app.get("/")
async def root():
    timestamp = str(datetime.now().isoformat())
    return {"message": f"{timestamp} {random_string}"}  
    