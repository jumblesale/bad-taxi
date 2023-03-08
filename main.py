from typing import *
from hamcrest import *


def taxi(starting_position: Tuple[int, int], tokens: str) -> Tuple[int, int]:
    return 0, 1


def test_moving_up():
    # assert
    token = 'u'

    # act
    result = taxi((0, 0), token)

    # assert
    assert_that(result, equal_to((0, 1)))
