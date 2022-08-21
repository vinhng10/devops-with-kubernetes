import os
import logging

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

PORT = os.environ.get('PORT', "NNNN")
logger = logging.getLogger("uvicorn.error")
logger.info(f"Server started in port {PORT}")

IMAGE_PATH = "/volume/image.png"

@app.get("/")
async def root():
    if os.path.exists(IMAGE_PATH):
        return FileResponse("/volume/image.png")
    else:
        return {"message": "Image is not downloaded."}