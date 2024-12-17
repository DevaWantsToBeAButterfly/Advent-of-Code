from aocd import get_data, submit

class Location:
    def __init__(self, x_coord, y_coord, location_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.location_type = location_type
        self.original_location_type = location_type
        self.visited = False
        self.can_be_reached = False

    def reset_location(self):
        self.location_type = self.original_location_type
        self.visited = False

class Guard:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.original_x_coord = x_coord
        self.original_y_coord = y_coord
        self.direction = 'up'
        self.visited_locations = 0
        self.loops_found = 0
        self.turn_spots = set()
        self.first_trip = True
        self.left = False
        self.is_looping = False

    def visit(self):
        current_location = puzzle_map[self.y_coord][self.x_coord]

        if not current_location.visited:
            if self.first_trip:
                current_location.visited = True
                current_location.can_be_reached = True
                self.visited_locations += 1

            if (self.x_coord == 0 or self.x_coord == len(puzzle_map[0]) - 1 or
                    self.y_coord == 0 or self.y_coord == len(puzzle_map)- 1):
                self.left = True


        if not self.left and not self.is_looping:
            self.move_or_turn()

    def move_or_turn(self):
        next_location_x_coord = self.x_coord + directions_offsets[self.direction][0]
        next_location_y_coord = self.y_coord + directions_offsets[self.direction][1]

        if puzzle_map[next_location_y_coord][next_location_x_coord].location_type == '#':
            self.turn()

            if (self.x_coord, self.y_coord, self.direction) in self.turn_spots:
                self.is_looping = True
                self.loops_found += 1
            else:
                self.turn_spots.add((self.x_coord, self.y_coord, self.direction))
        else:
            self.x_coord = next_location_x_coord
            self.y_coord = next_location_y_coord

    def turn(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'up'

    def respawn(self):
        self.x_coord = self.original_x_coord
        self.y_coord = self.original_y_coord
        self.direction = 'up'
        self.visited_locations = 0
        self.left = False
        self.is_looping = False
        self.turn_spots.clear()

directions_offsets = {'up':[0, -1], 'down':[0, 1], 'left':[-1, 0], 'right':[1, 0]}

puzzle_data = [list(row) for row in get_data(day=6, year=2024).splitlines()]

def build_map():
    new_map = []
    for row_index, row in enumerate(puzzle_data):
        new_map.append([])
        for node_index, node in enumerate(row):
            if node == '^':
                new_map[row_index].append(Location(node_index, row_index, '.'))
                guard = Guard(node_index, row_index)
            else:
                new_map[row_index].append(Location(node_index, row_index, node))

    return new_map, guard

def reset_map():
    guard.respawn()

    for row in puzzle_map:
        for location in row:
            location.reset_location()

def spawn_blocker(x_coord, y_coord):
    current_blocker = puzzle_map[y_coord][x_coord]
    if ((x_coord != guard.x_coord or y_coord != guard.y_coord) and
            current_blocker.location_type != '#' and
            current_blocker.can_be_reached):
        puzzle_map[y_coord][x_coord].location_type = '#'
        while not guard.left and not guard.is_looping:
            guard.visit()


puzzle_map, guard = build_map()

while not guard.left:
    guard.visit()

submit(guard.visited_locations, 'a')
guard.first_trip = False

for blocker_y_coord in range(len(puzzle_map)):
    for blocker_x_coord in range(len(puzzle_map[0])):
        reset_map()
        spawn_blocker(blocker_x_coord, blocker_y_coord)

submit(guard.loops_found, 'b')