from typing import *

from hamcrest import *


def taxi(starting_position: Tuple[int, int], tokens: str) -> Tuple[int, int]:
    if tokens == 'e':
        return 1, 0
    return 0, 1


'''
    Test list:
        - [X] N -> (0, 1)
        - [ ] E -> (1, 0)
        - [ ] S -> (0, -1)
        - [ ] W -> (-1, 0)
'''


def test_moving_up():
    # assert
    token = 'N'

    # act
    result = taxi((0, 0), token)

    # assert
    assert_that(result, equal_to((0, 1)))


def test_moving_east():
    # assert
    token = 'e'

    # act
    result = taxi((0, 0), token)

    # assert
    assert_that(result, equal_to((1, 0)))
