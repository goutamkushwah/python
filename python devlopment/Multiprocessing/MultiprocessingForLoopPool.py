# Tested on Python 3.11
from multiprocessing import Pool


def job(n):
    return n, n ** 3


if __name__ == "__main__":
    inputs = [k for k in range(4)]
    with Pool(2) as pool:
        results = pool.map(job, inputs)
    print(results)