from typing import *
from hamcrest import *
import pytest
import re

Coordinates = Tuple[int, int]
Direction = Literal['n', 'e', 's', 'w']
Velocity = NamedTuple('Velocity', [('speed',     int),
                                   ('direction', Direction)])
Movement = Callable[[Coordinates, Direction], Coordinates]


class BadTaxi:
    @staticmethod
    def taxi(starting_position: Coordinates, tokens: str) -> Coordinates:
        return BadTaxi.plan_trip(starting_position, tokens)[-1]

    @staticmethod
    def plan_trip(starting_position: Coordinates, tokens: str) -> List[Coordinates]:
        return list(BadTaxi.generate_coordinates(starting_position, Parser.parse(tokens)))

    @staticmethod
    def generate_coordinates(starting_position: Coordinates, velocities: List[Velocity]) -> Generator[Coordinates, None, None]:
        current_position = starting_position
        for velocity in velocities:
            speed = velocity.speed
            while speed > 0:
                speed = speed - 1
                current_position = BadTaxi.apply_direction(velocity.direction)(current_position)
                yield current_position

    @staticmethod
    def apply_direction(direction: Direction) -> Movement:
        def _move(x: int, y: int) -> Movement:
            def _step(_position: Coordinates) -> Coordinates:
                return _position[0] + x, _position[1] + y
            return _step

        def _direction_to_movement(_direction: Direction) -> Movement:
            return {
                'n': _move(0, 1),
                'e': _move(1, 0),
                's': _move(0, -1),
                'w': _move(-1, 0),
            }[_direction]

        return _direction_to_movement(direction)


class TestBadTaxi:
    @pytest.mark.parametrize("direction, expected", [
        ('n', (0, 1)),
        ('e', (1, 0)),
        ('s', (0, -1)),
        ('w', (-1, 0)),
    ])
    def test_cardinal_directions(self, direction: str, expected: Tuple[int, int]):
        # act
        final_position = TestBadTaxi.a_taxi_starting_from_0_0(direction)

        # assert
        assert_that(final_position, equal_to(expected))

    @pytest.mark.parametrize("movement, expected", [
        ('3n',         (0, 3)),
        ('4w2senenwn', (-3, 1)),
    ])
    def test_moving_in_a_direction_multiple_times(self, movement: str, expected: Tuple[int, int]):
        # act
        final_position = TestBadTaxi.a_taxi_starting_from_0_0(movement)

        # assert
        assert_that(final_position, equal_to(expected))

    @staticmethod
    def a_taxi_starting_from_0_0(tokens: str):
        return BadTaxi.taxi((0, 0), tokens)


class TestPlanningATrip:
    @pytest.mark.parametrize("starting_position, movement, expected_route", [
        ((1, -3), '3n2enw', [
            (1, 0),
            (3, 0),
            (3, 1),
            (2, 1),
        ]),
        ((-8, 2), '100w2se3n', [
            (-108, 2),
            (-108, 0),
            (-107, 0),
            (-107, 3),
        ]),
    ])
    def test_it_provides_a_plan_of_the_trip(
        self, starting_position: Coordinates, movement: str, expected_route: List[Coordinates]
    ):
        # act
        route_plan = BadTaxi.plan_trip(starting_position, movement)

        # assert
        assert_that(route_plan, equal_to(expected_route))


class Parser:
    @staticmethod
    def parse(tokens: str) -> List[Velocity]:
        velocities = []
        groups = re.findall(r'((\d+)([nswe]))+?|([nswe])', tokens.lower())
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
        assert_that(Parser.parse(tokens), equal_to(expected))
