AXIS_LIST = ['x', 'y', 'z']

moons_data = [
    {
        'name': 'Io',
        'vel': {
            'x': 0, 'y': 0, 'z': 0
        },
        'pos': {
            'x': 5, 'y': -1,  'z': 5
        },
    },
    {
        'name': 'Europa',
        'vel': {
            'x': 0, 'y': 0, 'z': 0
        },
        'pos': {
            'x': 0, 'y': -14, 'z': 2
        },
    },
    {
        'name': 'Ganymede',
        'vel': {
            'x': 0, 'y': 0, 'z': 0
        },
        'pos': {
            'x': 16, 'y': 4,  'z': 0
        },
    },
    {
        'name': 'Callisto',
        'vel': {
            'x': 0, 'y': 0, 'z': 0
        },
        'pos': {
            'x': 18, 'y': 1,  'z': 16
        },
    }
]


def update_universe(moons):

    moons = update_velocities(moons)
    moons = update_positions(moons)

    return moons


def update_velocities(moons):

    for moon in moons:
        for other_moon in [m for m in moons if m != moon]:
            for axis in AXIS_LIST:
                if moon['pos'][axis] < other_moon['pos'][axis]:
                    moon['vel'][axis] += 1

                elif moon['pos'][axis] > other_moon['pos'][axis]:
                    moon['vel'][axis] -= 1

    return moons


def update_positions(moons):
    for moon in moons:
        for axis in AXIS_LIST:
            moon['pos'][axis] += moon['vel'][axis]

    return moons


def calc_energy(moons):

    total_energy = 0

    for moon in moons:
        potential_energy = abs(moon['pos']['x']) + abs(moon['pos']['y']) + abs(moon['pos']['z'])
        kinetic_energy = abs(moon['vel']['x']) + abs(moon['vel']['y']) + abs(moon['vel']['z'])
        total_energy += potential_energy * kinetic_energy

    return total_energy


def solve(moons):

    for step in range(1000):
        moons = update_universe(moons)

    print(calc_energy(moons))
    print(moons)

solve(moons_data)