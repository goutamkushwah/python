# Tested on Python 3.11
from multiprocessing import Process


def greet(name, punctuation="."):
    msg = f"hello {name}{punctuation}"
    print(msg)


if __name__ == "__main__":
    p = Process(target=greet, args=("Goutam",), kwargs={"punctuation": "!"})
    p.start()
    p.join()