player_1_pos = 10
player_2_pos = 8


class Player:
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score


class GameState:
    def __init__(self):
        self.player_1_variants = []
        self.player_2_variants = []

    def new_turn_variants(self, player_1_vars, player_2_vars):
        self.player_1_variants = []
        self.player_2_variants = []
        for var in player_1_vars:
            self.player_1_variants.append(var)
        for var in player_2_vars:
            self.player_2_variants.append(var)


game_state = GameState()
player_1_variants = [Player(4, 0)]
player_2_variants = [Player(8, 0)]
keep_playing = True

# THIS GIVES A MEMORY ERROR SO DONT RUN IT PROBABLY
# def play_turn(current_variants):
#     new_variants = []
#     play_more = False
#     for move in range(3):
#         for variant in current_variants:
#             for dice_roll in range(1, 4):
#                 new_variant = Player(variant.pos + dice_roll, variant.score)
#                 new_variants.append(new_variant)
#         current_variants = new_variants.copy()
#         print(len(current_variants))
#         new_variants = []
#     print('end turn')
#
#     for variant in current_variants:
#         if variant.pos > 10:
#             variant.pos %= 10
#         variant.score += variant.pos
#
#     for variant in current_variants:
#         if variant.score < 21:
#             play_more = True
#             break
#
#     return current_variants, play_more


while keep_playing:
    game_state.new_turn_variants(player_1_variants, player_2_variants)

    player_1_variants, keep_playing = play_turn(player_1_variants)

    if not keep_playing:
        break

    player_2_variants = play_turn(player_2_variants)[0]

print(len(game_state.player_1_variants))
# for player_1_state, player_2_state in zip(game_state.player_1_variants, game_state.player_2_variants):
#     print(player_1_state.score, player_2_state.score)
