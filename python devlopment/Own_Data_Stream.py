import time
import random
from datetime import datetime

# Generator function for streaming data
def data_stream():
    while True:
        yield {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # human-readable time
            "value": random.randint(1, 100)  # random sensor-like value
        }
        time.sleep(1)  # simulate real-time delay

# Consume the stream
if __name__ == "__main__":
    for i, data in enumerate(data_stream()):
        print(data)
        if i == 20:  # stop after 20 values (safety limit)
            break
