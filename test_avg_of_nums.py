"""
# Averages of numbers
# Level: 7kyu
Problem Description: Write a method, that gets an array of integer-numbers and return an array of the
averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]

If the array has 0 or 1 values or is null or None, your method should return an empty array.

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""
from random import randrange

import pytest

from avg_of_nums import avg_range


def rand_iter(fn):
    """
    creates a random iterable
    returns the seed and the result of calling the test function on the seed
    """
    k = randrange(10)
    args = ([randrange(99) for k in range(k)],)
    return args + (fn(*args),)


k_res = [
    ([1, 3, 5, 1, -10], [2, 4, 3, -4.5]),
    rand_iter(avg_range),
    rand_iter(avg_range),
    rand_iter(avg_range),
    ([], []),
    ([1, None], []),
]


@pytest.mark.parametrize("k,result", k_res)
def test_unit(k, result):
    assert avg_range(k) in [result, list(result)]
