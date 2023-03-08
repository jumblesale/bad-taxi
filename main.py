from typing import *

from hamcrest import *


def taxi(starting_position: Tuple[int, int], tokens: str) -> Tuple[int, int]:
    if tokens == 'e':
        return 1, 0
    return 0, 1


class TestTaxi:
    """
        Test list:
            - [X] N -> (0, 1)
            - [X] E -> (1, 0)
            - [ ] S -> (0, -1)
            - [ ] W -> (-1, 0)
    """

    def test_moving_north(self):
        # assert
        token = 'N'

        # act
        result = a_taxi_starting_from_0_0()(token)

        # assert
        assert_that_the_location_is(result, 0, 1)

    def test_moving_east(self):
        # assert
        token = 'e'

        # act
        result = a_taxi_starting_from_0_0()(token)

        # assert
        assert_that_the_location_is(result, 1, 0)

    def test_moving_south(self):
        # assert
        token = 's'

        # act
        result = a_taxi_starting_from_0_0()(token)

        # assert
        assert_that_the_location_is(result, 0, -1)


def a_taxi_starting_from_0_0():
    return lambda x: taxi((0, 0), x)


def assert_that_the_location_is(result: Tuple[int, int], x: int, y: int):
    assert_that(result, equal_to((x, y)))
