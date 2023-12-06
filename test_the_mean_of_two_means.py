#!/usr/bin/env python

import pytest

from the_mean_of_two_means import get_mean

nxy_res = [
    ([1, 3, 2, 4], 2, 3, 2.5),
    ([1, 3, 2, 4], 1, 2, -1),
    ([1, 3, 2, 4], 2, 8, -1),
]


@pytest.mark.parametrize("arr,x,y, result", nxy_res)
def test_unit(arr, x, y, result):
    assert get_mean(arr, x, y) == result
