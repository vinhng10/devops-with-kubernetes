import os
import logging

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

PORT = os.environ.get('PORT', "NNNN")
logger = logging.getLogger("uvicorn.error")
logger.info(f"Server started in port {PORT}")

IMAGE_PATH = "/volume/image.png"

@app.get("/", response_class=HTMLResponse)
async def root():
    return f"""
    <html>
        <head>
            <title>Todo</title>
        </head>
        <body>
            <img src="{IMAGE_PATH}" style="width:300px;height:300px;>
            <form>
                <input type="text" name="todo" maxlength=140>
                <input type="submit" value="Create TODO>
            </form>
            <ul>
                <it>TODO 1</it>
                <it>TODO 2</it>
            </ul>
        </body>
    </html>
    """
