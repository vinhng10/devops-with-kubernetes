import os
from fastapi import FastAPI

# Create an app:
app = FastAPI()

# Counter:
counter = -1

os.makedirs("/volume", exist_ok=True)
@app.get("/pingpong")
async def root():
    global counter

    counter += 1
    with open("/volume/ping-pong.txt", "w") as f:
        f.write(str(counter))

    return f"pong {counter}" 
    