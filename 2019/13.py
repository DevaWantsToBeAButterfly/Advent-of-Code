from intcode_computer import IntcodeComputer

class ArcadeCabinet():
    def __init__(self):
        self.tiles = []

    def spawn_tiles(self, tiles_data):
        tiles_list = self.rewrite_tile_data(tiles_data)

        for tile in tiles_list:
            self.tiles.append(Tile(tile[0], tile[1], tile[2]))

    def rewrite_tile_data(self, tiles_data):
        tiles_list = []

        for n in range(0, len(tiles_data), 3):
            tiles_list.append(tiles_data[n:n+3])

        return tiles_list

    def count_objects(self, object):
        count = 0

        for tile in self.tiles:
            if tile.object == object:
                count += 1

        return count


class Tile():
    def __init__(self, x_coord, y_coord, object_id):
        self.tile_objects = ['Empty', 'Wall', 'Block', 'Paddle', 'Ball']
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.object = self.tile_objects[object_id]


with open('data_files\day_13_input.txt') as input_file:
    puzzle_input = [int(num) for num in input_file.read().split(',')]

arcade = ArcadeCabinet()
intComp = IntcodeComputer(puzzle_input, False)
tiles_data = intComp.execute_program()
arcade.spawn_tiles(tiles_data)
print(arcade.count_objects('Block'))