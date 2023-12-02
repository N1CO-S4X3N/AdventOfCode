import os
import sys


games = {}


with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        result = line.strip().split(': ')
        contents = result[1].split('; ')
        sets = [s.split(', ') for s in contents]
        games.update({result[0]: sets})


def count_colors(game_set):
    red, green, blue = 0, 0, 0
    for draw in game_set:
        for color_amount in draw:
            nbr, color = color_amount.split(' ')
            nbr = int(nbr)
            if color == 'red':
                if nbr > red:
                    red = nbr
            elif color == 'green':
                if nbr > green:
                    green = nbr
            elif color == 'blue':
                if nbr > blue:
                    blue = nbr
    return red * green * blue


def process_games():
    totals = []
    for sets in games.values():
        totals.append(count_colors(sets))
    return sum(totals)


print("total: ", process_games())
