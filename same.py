from typing import List


def comp(a: List[int], b: List[int]) -> bool:
    """
    for each index of a return true if i pow 2 is in b; sorted min/max defines
    the order of argument and all extracts truthiness from the map.
    """
    args = sorted(a), sorted(b)
    return all(
        map(
            lambda i: True if i**2 in max(args) else False,
            min(args),
        )
    )
