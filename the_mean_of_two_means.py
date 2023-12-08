from typing import List, Optional


def get_mean(arr: List[Optional[int]], x: int, y: int) -> Optional[float]:
    """
    Returns the mean of the means of the first x and last y elements of arr.

    >>> get_mean([1, 3, 2, 4], 2, 3)
    2.5
    >>> get_mean([1, 3, 2, 4], 1, 2)
    >>> get_mean([1, 3, 2, 4], 2, 8)
    """
    # Validate the input parameters
    if not (2 <= x <= len(arr) and 2 <= y <= len(arr)):
        return None

    # Calculate the mean of the first x elements
    mean_x = sum(arr[:x]) / x

    # Calculate the mean of the last y elements
    mean_y = sum(arr[-y:]) / y

    # Return the mean of the two means
    return (mean_x + mean_y) / 2
