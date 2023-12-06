#!/usr/bin/env python
from functools import reduce


def get_mean(arr, x, y):
    """
    # The mean of two means
    # Level: 7kyu
    Write a function getMean that takes as parameters an array (arr) and 2 integers (x and y). The function should return the mean between the mean of the the first x elements of the array and the mean of the last y elements of the array.

    The mean should be computed if both x and y have values higher than 1 but less or equal to the array's length. Otherwise the function should return -1.

    getMean([1,3,2,4], 2, 3) should return 2.5 because: the mean of the the first 2 elements of the array is (1+3)/2=2 and the mean of the last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.

    getMean([1,3,2,4], 1, 2) should return -1 because x is not higher than 1.

    getMean([1,3,2,4], 2, 8) should return -1 because 8 is higher than the array's length.
    """
    if any(len(arr) <= i or i < 2 for i in [x, y]):
        return -1
    return reduce(lambda x, y: x + sum(arr[:y]) / 2, [0, x, y]) / 2
