
import math
import multiprocessing
from itertools import chain, combinations, islice, permutations


def test_multthread():
    manager = multiprocessing.Manager()
    return_dict = manager.list()
    jobs = []
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict)


def worker(chunk, return_list):
    """worker function"""
    value = 0
    for i in chunk:
        print(i, end='')
        value += sum(i)
    print()
    return_list.append(value)


def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))


def test_multithread_combination():
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    n = 5
    r = 2

    c = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print("Total combinations:", c)
    combos = combinations(range(n), r)
    slice = c//2
    J = 0
    for i, chunk in enumerate(chunks(combos, slice)):
        if i % slice == 0:
            J += 1
            print("Number of processes:", J)
            p = multiprocessing.Process(target=worker, args=(chunk, return_list))
            jobs.append(p)
            p.start()

    for proc in jobs:
        proc.join()
    print(sorted(return_list))


if __name__ == "__main__":
    test_multithread_combination()
