from fastapi import FastAPI

# Create an app:
app = FastAPI()

# Counter:
counter = -1

@app.get("/pingpong")
async def root():
    global counter
    counter += 1
    return f"pong {counter}" 
    