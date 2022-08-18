import os
import logging
import time
from datetime import datetime

# Log the port of the server:
PORT = os.environ.get('PORT', "NNNN")
logger = logging.getLogger("uvicorn.error")
logger.info(f"Server started in port {PORT}")

os.makedirs("/volume", exist_ok=True)
while True:
    with open("/volume/timestamp.txt", "w") as f:
        f.write(str(datetime.now().isoformat()))
    time.sleep(5)  
    