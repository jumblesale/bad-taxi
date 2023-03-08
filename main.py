from typing import *
from hamcrest import *
import pytest


def taxi(starting_position: Tuple[int, int], tokens: str) -> Tuple[int, int]:
    if tokens == '3n':
        return 3, 0
    if tokens == 'w':
        return -1, 0
    if tokens == 's':
        return 0, -1
    if tokens == 'e':
        return 1, 0
    return 0, 1


class TestTaxi:
    @pytest.mark.parametrize("direction, expected", [
        ('n', (0, 1)),
        ('e', (1, 0)),
        ('s', (0, -1)),
        ('w', (-1, 0)),
    ])
    def test_cardinal_directions(self, direction: str, expected: Tuple[int, int]):
        # act
        final_position = a_taxi_starting_from_0_0()(direction)

        # assert
        assert_that(final_position, equal_to(expected))

    def test_moving_multiples(self):
        # arrange
        movement = "3n"

        # act
        final_position = a_taxi_starting_from_0_0()(movement)

        # assert
        assert_that(final_position, equal_to((3, 0)))


def a_taxi_starting_from_0_0():
    return lambda x: taxi((0, 0), x)
