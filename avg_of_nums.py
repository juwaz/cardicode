from typing import List, Union, Optional


def avg_range(k: List[Optional[int]]) -> List[Union[int, float]]:
    """
    Returns a list of the average of each pair of adjacent elements in k.

    >>> avg_range([1, 2, 3, 4])
    [1.5, 2.5, 3.5]
    >>> avg_range([None, 2, 3, 4])
    []
    >>> avg_range([1])
    []
    """
    # Check for invalid input
    if None in k or len(k) < 2:
        return []

    # Use list comprehension instead of map and lambda
    h = [(k[i] + k[i + 1]) / 2 for i in range(len(k) - 1)]

    return h
