#!/usr/bin/env python

import pytest
from replace_with_alphabet_position import alphabet_position

s_res = [
    (
        "The sunset sets at twelve o' clock.",
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
    )
]


@pytest.mark.parametrize("s,res", s_res)
def test_unit(s, res):
    assert alphabet_position(s) == res
