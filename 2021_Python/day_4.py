class BingoBoard:
    def __init__(self, nums_list):
        self.board = [[num for num in nums_row.split()] for nums_row in nums_list]
        self.scoreboard = [[False for _ in nums_row] for nums_row in self.board]
        self.score = 0

    def check_if_scored(self, drawn_number):
        for row_index, row in enumerate(self.board):
            for num_index, num in enumerate(row):
                if num == drawn_number:
                    self.scoreboard[row_index][num_index] = True
                    return

    def check_if_won(self):
        for n in range(5):
            row = self.scoreboard[n]
            column = [row[n] for row in self.scoreboard]

            for group in [row, column]:
                if all(is_found for is_found in group):
                    return True

    def count_score(self):
        for n in range(5):
            for number, is_found in zip(self.board[n], self.scoreboard[n]):
                if not is_found:
                    self.score += int(number)


with open('data_files/day_4_input.txt') as input_file:
    data_list = input_file.read().splitlines()

draws_list = data_list[0].split(',')


def generate_boards(data):
    lst = []
    for bingo_board_start in range(2, len(data) - 2, 6):
        lst.append(BingoBoard(data[bingo_board_start:bingo_board_start + 5]))
    return lst


def find_winning_board(lst):
    for draw in draws_list:
        for bingo_board in lst:
            bingo_board.check_if_scored(draw)
            if bingo_board.check_if_won():
                bingo_board.count_score()
                return bingo_board.score * int(draw)


def find_losing_board(lst):
    for draw in draws_list:
        updated_boards_list = []
        for bingo_board in lst:
            latest_board = bingo_board
            bingo_board.check_if_scored(draw)
            if not bingo_board.check_if_won():
                updated_boards_list.append(bingo_board)

        lst = updated_boards_list
        latest_draw = draw
        if not lst:
            break

    latest_board.count_score()
    return latest_board.score * int(latest_draw)


boards_list = generate_boards(data_list)
print(find_winning_board(boards_list))

boards_list = generate_boards(data_list)
print(find_losing_board(boards_list))
