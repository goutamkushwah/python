# Tested on Python 3.11
import time
from multiprocessing import Process


def slow_worker():
    time.sleep(60)


if __name__ == "__main__":
    p = Process(target=slow_worker)
    p.start()
    time.sleep(0.1)
    p.terminate()
    p.join()
    print("exitcode after terminate:", p.exitcode)