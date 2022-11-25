from typing import List


def array_diff(arg1: List[str | int], arg2=List[str | int]) -> List[str | int]:
    """
    using builtin set.difference and list to return the desired type
    """
    return list(set(arg1).difference(arg2))
