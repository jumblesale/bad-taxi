import random

from bad_taxi.trip_planner import BadTaxi


def generate_directions(use_multipliers: bool = True):
    if use_multipliers:
        multiplier = random.choice(['', random.choice([random.randint(2, 17), random.randint(2, 999)])])
    else:
        multiplier = ''
    direction = random.choice(['n', 'e', 's', 'w'])
    return f'{multiplier}{direction}'


def generate_complex_trip(steps):
    x = random.randint(-3968, 40022)
    y = random.randint(-17603, 2239)
    starting_position = (x, y)
    tokens = ''.join([generate_directions() for _ in range(steps)])
    locations = BadTaxi.plan_trip(starting_position, tokens)
    return starting_position, tokens, locations


def generate_simple_trip(steps):
    tokens = ''.join([generate_directions(False) for _ in range(steps)])
    locations = BadTaxi.taxi((0, 0), tokens)
    return tokens, locations


if __name__ == "__main__":
    print('simple trip:')
    data = generate_simple_trip(3000)
    print('\n'.join([
        data[0],
        f'({data[1][0]}, {data[1][1]})'
    ]))
    print('complex trip:')
    data = generate_complex_trip(1000)
    print('\n'.join([
        f'({data[0][0]}, {data[0][1]})',
        data[1],
        str(data[2][10101]),
    ]))
