SHAPE_DATA = {'A': {'Name': 'Rock', 'Score': 1}, 'X': {'Name': 'Rock', 'Score': 1},
              'B': {'Name': 'Paper', 'Score': 2}, 'Y': {'Name': 'Paper', 'Score': 2},
              'C': {'Name': 'Scissors', 'Score': 3}, 'Z': {'Name': 'Scissors', 'Score': 3}}

ROUND_OUTCOME_SCORES = {'Win': 6, 'Draw': 3, 'Lose': 0}


with open('.\data_files\day_2_input.txt') as input_file:
    game_instructions = input_file.readlines()
input_file.close()


def check_outcome(elf_shape, player_shape):
    elf_shape = SHAPE_DATA[elf_shape]['Name']
    player_shape = SHAPE_DATA[player_shape]['Name']

    if elf_shape == 'Rock':
        if player_shape == 'Paper':
            return 'Win'
        elif player_shape == 'Scissors':
            return 'Lose'
    elif elf_shape == 'Paper':
        if player_shape == 'Rock':
            return 'Lose'
        elif player_shape == 'Scissors':
            return 'Win'
    elif elf_shape == 'Scissors':
        if player_shape == 'Rock':
            return 'Win'
        elif player_shape == 'Paper':
            return 'Lose'

    return 'Draw'


def update_score(current_score, round_outcome, player_shape):
    return current_score + ROUND_OUTCOME_SCORES[round_outcome] + SHAPE_DATA[player_shape]['Score']


def iterate_rounds(game_data, score):
    for round_instructions in game_data:
        outcome = check_outcome(round_instructions[0], round_instructions[2])
        score = update_score(score, outcome, round_instructions[2])

    return score


print(iterate_rounds(game_instructions, 0))
