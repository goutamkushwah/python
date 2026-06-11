# Tested on Python 3.11
from multiprocessing import Pool


def add(a, b):
    return a + b


if __name__ == "__main__":
    with Pool(2) as pool:
        res = pool.apply_async(add, (2, 3))
        other = pool.apply_async(add, (40, 2))
        print("first:", res.get())
        print("second:", other.get())