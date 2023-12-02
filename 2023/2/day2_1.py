import os
import sys


games = {}
limits = {'red': 12, 'green': 13, 'blue': 14}


with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        result = line.strip().split(': ')
        contents = result[1].split('; ')
        sets = [s.split(', ') for s in contents]
        games.update({result[0]: sets})

def is_game_possible(game_set):
    for draw in game_set:
        for color_amount in draw:
            nbr, color = color_amount.split(' ')
            if int(nbr) > limits[color]:
                return False
    return True


def process_games():
    possible = 0
    impossible = 0
    for game, sets in games.items():
        possible_game = is_game_possible(sets)
        if possible_game:
            possible += int(game.split(' ')[1])
        else:
            impossible += int(game.split(' ')[1])
    return possible, impossible


possible, impossible = process_games()
print("POSSIBLE: ", possible)
print("IMPOSSIBLE: ", impossible)