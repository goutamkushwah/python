# Tested on Python 3.11
from multiprocessing import Pool


def square(x):
    return x * x


if __name__ == "__main__":
    with Pool(4) as pool:
        out = pool.map(square, range(6))
    print(out)