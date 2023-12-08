from typing import List, Union


def array_diff(
    arg1: List[Union[str, int]], arg2: List[Union[str, int]]
) -> List[Union[str, int]]:
    """
    Returns a list of the elements from arg1 that are not in arg2.

    >>> array_diff([1, 2, 3], [2, 4])
    [1, 3]
    >>> array_diff(["a", "b", "c"], ["b", "d"])
    ['a', 'c']
    >>> array_diff([1, "a", 3], [None, 4])
    Traceback (most recent call last):
    ValueError: Invalid element: None
    """
    # Validate the arguments
    for arg in (arg1, arg2):
        for elem in arg:
            if not isinstance(elem, (str, int)):
                raise ValueError(f"Invalid element: {elem}")

    return [elem for elem in arg1 if elem not in arg2]
