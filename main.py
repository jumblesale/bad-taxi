from typing import *
from hamcrest import *
import pytest
import re

Coordinates = Tuple[int, int]
Movement = Callable[[Coordinates], Coordinates]
Direction = Literal['n', 'e', 's', 'w']
Velocity = NamedTuple('Velocity', [('speed', int),
                                   ('direction', Direction)])


def taxi(starting_position: Coordinates, tokens: str) -> Coordinates:
    def _move(x: int, y: int) -> Movement:
        def _step(start: Coordinates, speed: int) -> Coordinates:
            return start[0] + x * speed, start[1] + y * speed
        return _step

    def _velocity_to_movement(direction: Direction) -> Movement:
        return {
            'n': _move(0, 1),
            'e': _move(1, 0),
            's': _move(0, -1),
            'w': _move(-1, 0),
        }[direction]

    velocities: List[Velocity] = parse(tokens)

    for velocity in velocities:
        starting_position = _velocity_to_movement(velocity.direction) \
            (starting_position, velocity.speed)

    return starting_position


def plan_trip(starting_position: Coordinates, tokens: str) -> List[Coordinates]:
    pass


class TestTaxi:
    @pytest.mark.parametrize("direction, expected", [
        ('n', (0, 1)),
        ('e', (1, 0)),
        ('s', (0, -1)),
        ('w', (-1, 0)),
    ])
    def test_cardinal_directions(self, direction: str, expected: Tuple[int, int]):
        # act
        final_position = TestTaxi.a_taxi_starting_from_0_0()(direction)

        # assert
        assert_that(final_position, equal_to(expected))

    @pytest.mark.parametrize("movement, expected", [
        ('3n', (0, 3)),
        ('4w2senenwn', (-3, 1)),
    ])
    def test_moving_multiples(self, movement: str, expected: Tuple[int, int]):
        # act
        final_position = TestTaxi.a_taxi_starting_from_0_0()(movement)

        # assert
        assert_that(final_position, equal_to(expected))

    @staticmethod
    def a_taxi_starting_from_0_0():
        return lambda x: taxi((0, 0), x)


class TestPlanningATrip():
    def test_it_provides_a_plan_of_the_trip(self):
        # arrange
        starting_position = (1, -3)
        tokens = "3n2enw"
        expected_route = [
            (4, -3),
            (4, -1),
            (5, -1),
            (5, -2),
        ]

        # act
        result = plan_trip(starting_position, tokens)

        # assert
        assert_that(result, equal_to(expected_route))


def parse(tokens: str) -> List[Velocity]:
    velocities = []
    groups = re.findall(r'((\d+)([nswe]))+?|([nswe])', tokens)
    for _, speed, multiple_direction, single_direction in groups:
        if speed:
            velocities.append(Velocity(int(speed), multiple_direction))
        elif single_direction:
            velocities.append(Velocity(1, single_direction))
    return velocities


class TestParse:
    @pytest.mark.parametrize("tokens, expected", [
        ('n',       [Velocity(1, 'n')]),
        ('e',       [Velocity(1, 'e')]),
        ('s',       [Velocity(1, 's')]),
        ('w',       [Velocity(1, 'w')]),
        ('ne',      [Velocity(1, 'n'), Velocity(1, 'e')]),
        ('sw',      [Velocity(1, 's'), Velocity(1, 'w')]),
        ('3ne',     [Velocity(3, 'n'), Velocity(1, 'e')]),
        ('4s2ne2n', [Velocity(4, 's'), Velocity(2, 'n'), Velocity(1, 'e'), Velocity(2, 'n')]),
    ])
    def test_it_parses_directions_to_velocities(self, tokens: str, expected: List[Velocity]):
        assert_that(parse(tokens), equal_to(expected))
