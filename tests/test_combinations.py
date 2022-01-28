import timeit
from itertools import combinations

import numpy
from make_poffins.berry.berry_library import every_berry
from make_poffins.constants import calculate_time


def itertools_combo(every_berry, n):
    return combinations(every_berry, n)


def n_length_combo(iterable, r):

    char = tuple(iterable)
    n = len(char)

    if r > n:
        return

    index = numpy.arange(r)

    # returns the first sequence
    yield tuple(char[i] for i in index)

    while True:

        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return

        index[i] += 1

        for j in range(i + 1, r):

            index[j] = index[j-1] + 1

        yield tuple(char[i] for i in index)


@calculate_time
def test_numpy_method():
    for x, y in enumerate(n_length_combo(every_berry, 4)):
        pass


@calculate_time
def test_itertools_method():
    for x, y in enumerate(itertools_combo(every_berry, 4)):
        pass


if __name__ == "__main__":
    test_numpy_method()
    test_itertools_method()
