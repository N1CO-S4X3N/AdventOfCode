import os
import sys


class Number():
    def __init__(self, number, positions):
        self.positions = positions
        self.number = number
    
    def check_adjacent(self):
        self.is_correct = False
        for xy in self.positions:
            if self.is_correct:
                break
            for pos in symbol_positions:
                # check same row
                if pos[0] == xy[0] and (pos[1] == xy[1] + 1 or pos[1] == xy[1] - 1):
                    self.is_correct = True
                    break
                # check row above
                elif pos[0] == xy[0] - 1 and pos[1] == xy[1]:
                    self.is_correct = True
                    break
                # check row below
                elif pos[0] == xy[0] + 1 and pos[1] == xy[1]:
                    self.is_correct = True
                    break
                # check upper left corner
                elif pos[0] == xy[0] - 1 and pos[1] == xy[1] - 1:
                    self.is_correct = True
                    break
                # check upper right corner
                elif pos[0] == xy[0] - 1 and pos[1] == xy[1] + 1:
                    self.is_correct = True
                    break
                # check lower left corner
                elif pos[0] == xy[0] + 1 and pos[1] == xy[1] - 1:
                    self.is_correct = True
                    break
                # check lower right corner
                elif pos[0] == xy[0] + 1 and pos[1] == xy[1] + 1:
                    self.is_correct = True
                    break


matrix = []
numbers = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        newline = [c for c in line.strip()]
        matrix.append(newline)


for i, row in enumerate(matrix):
    number = ''
    position = []
    for j, cell in enumerate(row):
        if cell.isdigit():
            number += cell
            position.append((i, j))
        else:
            position = []
            number = ''
        if len(position) > 0 and (j == len(row) - 1 or (j < len(row) - 1 and not row[j+1].isdigit())):
            numbers.append(Number(int(number), position))

    
def get_symbol_positions():
    positions = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if not cell.isdigit() and cell != '.':
                positions.append((i, j))
    return positions

symbol_positions = get_symbol_positions()


total = 0
for n in numbers:
    n.check_adjacent()
    if n.is_correct:
        total += n.number

print("TOTAL: ", total)