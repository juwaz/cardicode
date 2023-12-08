from typing import List


def rect_to_square(length: int, width: int) -> List[int]:
    """
    Cut a rectangle into squares and return the sizes of the squares.

    Args:
        length (int>0): The length of the rectangle.
        width (int>0): The width of the rectangle.

    Returns:
        List[int]: A list of the sizes of the squares.

    Examples:
        >>> rect_to_square(5, 3)
        [3, 2, 1, 1]
        >>> rect_to_square(3, 5)
        [3, 2, 1, 1]
        >>> rect_to_square(-1, 5)
        Traceback (most recent call last):
        ValueError: length and width must be positive integers.

    """
    if length == width:
        return [length]
    elif (
        length <= 0
        or width <= 0
        or not isinstance(length, int)
        or not isinstance(width, int)
    ):
        raise ValueError("length and width must be positive integers.")

    else:
        smaller_side = min(length, width)
        difference = abs(length - width)
        return [smaller_side] + rect_to_square(smaller_side, difference)
