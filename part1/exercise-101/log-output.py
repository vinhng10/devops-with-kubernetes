import uuid
import time
from datetime import datetime


if __name__ == "__main__":
    random_string = uuid.uuid1()
    while True:
        timestamp = str(datetime.now().isoformat())
        print(f"{timestamp} {random_string}")
        time.sleep(5)
    
    