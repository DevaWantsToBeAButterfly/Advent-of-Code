from aocd import get_data, submit, puzzle

class Location:
    def __init__(self, x_coord, y_coord, location_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.location_type = location_type
        self.visited = False

class Guard:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = 'up'
        self.visited_locations = 0
        self.left = False

    def visit(self):
        current_location = puzzle_map[self.y_coord][self.x_coord]
        if not current_location.visited:
            puzzle_map[self.y_coord][self.x_coord].visited = True
            self.visited_locations += 1
            if (self.x_coord == 0 or self.x_coord == len(puzzle_map[0]) - 1 or
                    self.y_coord == 0 or self.y_coord == len(puzzle_map)- 1):
                self.leave()

    def move_or_turn(self):
        next_location_x_coord = self.x_coord + directions_offsets[self.direction][0]
        next_location_y_coord = self.y_coord + directions_offsets[self.direction][1]

        if puzzle_map[next_location_y_coord][next_location_x_coord].location_type == '#':
            self.turn()
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

    def leave(self):
        self.leave = True
        submit(self.visited_locations, 'a')

directions_offsets = {'up':[0, -1], 'down':[0, 1], 'left':[-1, 0], 'right':[1, 0]}

puzzle_data = [list(row) for row in get_data(day=6, year=2024).splitlines()]
puzzle_map = []

for row_index, row in enumerate(puzzle_data):
    puzzle_map.append([])
    for node_index, node in enumerate(row):
        if node == '^':
            puzzle_map[row_index].append(Location(node_index, row_index, '.'))
            guard = Guard(node_index, row_index)
        else:
            puzzle_map[row_index].append(Location(node_index, row_index, node))

while not guard.left:
    guard.visit()
    guard.move_or_turn()

