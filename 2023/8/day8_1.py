import os
import sys


network = {}
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        if i == 0:
            sequence = line
        newline = line.split('=')
        if i > 1:
            destinations = newline[1].lstrip().replace('(', '').replace(')', '')
            network.update({newline[0].strip(): (newline[1][2:5], newline[1][7:10])})

found_end = False
next_up = 'AAA'
count = 0
while not found_end:
    for direction in sequence:
        key = 0 if direction == 'L' else 1
        next_up = network[next_up][key]
        count += 1
        if next_up == 'ZZZ':
            found_end = True

print("count: ", count)