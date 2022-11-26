from typing import List


def avg_range(k: List[int]) -> List[int | float]:
    """
    start with a typeerror catch of bad input
    use an index aware wrap
    for each index add it's +1 neighbor and divide the result by 2
    """
    try:
        if None in k or len(k) < 2:
            raise TypeError
    except TypeError:
        return []

    k_i = {i: n for i, n in enumerate(k)}

    h = list(map(lambda i: (k[i] + k[i + 1]) / 2, list(k_i.keys())[:-1]))

    return h
