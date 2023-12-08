from typing import List


def compare_squares(a: List[int], b: List[int]) -> bool:
    """
    Compare two lists of integers and return True if every element in the first list
    is the square of an element in the second list, regardless of the order.

    Parameters:
        a (List[int]): The first list of integers
        b (List[int]): The second list of integers

    Returns:
        bool: True if the condition is met, False otherwise

    Example:
        >>> compare_squares([1, 4, 9], [9, 16, 1])
        False
        >>> compare_squares([2, 3, 4], [4, 9, 16])
        True
        >>> compare_squares([9, 0, 2], [4, 81, 0])
        True
    """
    a = sorted(a)
    b = sorted(b)
    return all(i**2 in b for i in a)
