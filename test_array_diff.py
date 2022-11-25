"""
# Array.diff
# Level: 6kyu
Problem Description:Your goal in this kata is to implement an difference function, which subtracts one list from
another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""
import pytest

from array_diff import array_diff
from itertools import permutations

a_b_result = [
    ([1, 2], [1], [2]),
    ([1, 2, 2, 2, 3], [2], [1, 3]),
    ([1, "2", "3", 3], [3, 4, 5], list(permutations([1, "2", "3"]))),
    ([3, 4, 5], [1, "2", "3", 3], [4, 5]),
]


@pytest.mark.parametrize("a,b, result", a_b_result)
def test_unit(a, b, result):
    assert (
        array_diff(a, b) in [result, tuple(result)] or tuple(array_diff(a, b)) in result
    )
