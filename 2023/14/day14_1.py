import os
import sys

map = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        map.append([l for l in line])

new_map = map.copy()
for i, stones in enumerate(map):
    last_free_slot = None
    for pos, stone in enumerate(stones):
        if stone != 'O':
            continue
        for ind in reversed(range(0, i)):
            if new_map[ind][pos] != '.':
                if ind == i-1:
                    last_free_slot = None
                break
            else:
                last_free_slot = (ind, pos)
        if last_free_slot:
            new_map[last_free_slot[0]][last_free_slot[1]] = 'O'
            new_map[i][pos] = '.'

total = 0
for count, row in enumerate(reversed(new_map), start=1):
    total += count * row.count('O')

print(total)
