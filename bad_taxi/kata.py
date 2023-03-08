import random

from trips import plan_trip


def generate_direction():
    multiplier = random.choice(['', random.choice([random.randint(2, 17), random.randint(2, 999)])])
    direction = random.choice(['n', 'e', 's', 'w'])
    return f'{multiplier}{direction}'


def generate_random_trip(steps):
    x = random.randint(-3968, 40022)
    y = random.randint(-17603, 2239)
    starting_position = (x, y)
    tokens = ''.join([generate_direction() for _ in range(steps)])
    locations = plan_trip(starting_position, tokens)
    return starting_position, tokens, locations


if __name__ == "__main__":
    data = generate_random_trip(1000)
    print('\n'.join([
        f'({data[0][0]}, {data[0][1]})',
        data[1],
        '\n'.join([f'({l[0]}, {l[1]})' for l in data[2]])])
    )
