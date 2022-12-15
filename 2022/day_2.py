SHAPE_DATA = {'A': {'Name': 'Rock', 'Score': 1}, 'X': {'Name': 'Rock', 'Score': 1},
              'B': {'Name': 'Paper', 'Score': 2}, 'Y': {'Name': 'Paper', 'Score': 2},
              'C': {'Name': 'Scissors', 'Score': 3}, 'Z': {'Name': 'Scissors', 'Score': 3}}
ROUND_OUTCOME_DATA = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
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


def choose_shape_to_play(elf_shape_id, round_outcome):
    elf_shape = SHAPE_DATA[elf_shape_id]['Name']

    if round_outcome == 'Win':
        if elf_shape == 'Rock':
            return 'Y'
        elif elf_shape == 'Paper':
            return 'Z'
        else:
            return 'X'

    elif round_outcome == 'Lose':
        if elf_shape == 'Rock':
            return 'Z'
        elif elf_shape == 'Paper':
            return 'X'
        else:
            return 'Y'
    else:
        if elf_shape == 'Rock':
            return 'X'
        elif elf_shape == 'Paper':
            return 'Y'
        else:
            return 'Z'


def update_score(current_score, round_outcome, player_shape):
    return current_score + ROUND_OUTCOME_SCORES[round_outcome] + SHAPE_DATA[player_shape]['Score']


def iterate_rounds(game_data, score, part_id):
    for round_instructions in game_data:
        elf_shape_id = round_instructions[0]
        if part_id == 1:
            player_shape_id = round_instructions[2]
            round_outcome = check_outcome(elf_shape_id, player_shape_id)
        elif part_id == 2:
            round_outcome = ROUND_OUTCOME_DATA[round_instructions[2]]
            player_shape_id = choose_shape_to_play(elf_shape_id, round_outcome)

        score = update_score(score, round_outcome, player_shape_id)

    return score


print('The total score is', iterate_rounds(game_instructions, 0, 1))
print('The total score is', iterate_rounds(game_instructions, 0, 2))
