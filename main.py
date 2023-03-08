from typing import *
from hamcrest import *
import pytest

Coordinates = Tuple[int, int]


def taxi(starting_position: Coordinates, tokens: str) -> Coordinates:
    def move(x: int, y: int) -> Callable[[Coordinates], Coordinates]:
        def step(start: Coordinates) -> Coordinates:
            return start[0] + x, start[1] + y
        return step

    direction_to_movement_map = {
        'n': move(0, 1),
        'e': move(1, 0),
        's': move(0, -1),
        'w': move(-1, 0),
    }

    return direction_to_movement_map[tokens](starting_position)


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

    @pytest.mark.parametrize("movement, expected", [
        ('3n', (3, 0)),
        ('4w2s', (-2, -4)),
    ])
    @pytest.mark.skip
    def test_moving_multiples(self, movement: str, expected: Tuple[int, int]):
        # act
        final_position = a_taxi_starting_from_0_0()(movement)

        # assert
        assert_that(final_position, equal_to(expected))


def a_taxi_starting_from_0_0():
    return lambda x: taxi((0, 0), x)
