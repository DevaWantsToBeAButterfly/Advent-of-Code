import sys

player_1_pos = 10
player_2_pos = 8


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0

    def move(self, steps):
        self.pos += steps
        if self.pos > 10:
            self.pos %= 10
            if self.pos == 0:
                self.pos = 10

    def end_turn(self):
        self.score += self.pos


class Dice:
    def __init__(self):
        self.value = 1
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        self.value += 1
        if self.value > 100:
            self.value = 1


def play_turn(turn_player, other_player):
    for dice_roll in range(3):
        turn_player.move(dice.value)
        dice.roll()

    turn_player.end_turn()

    if turn_player.score >= 1000:
        print(other_player.score * dice.rolls)
        sys.exit()


player_1 = Player(player_1_pos)
player_2 = Player(player_2_pos)
dice = Dice()

while True:
    play_turn(player_1, player_2)
    play_turn(player_2, player_1)
