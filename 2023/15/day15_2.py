import os
import sys

hashmap = {}
for i in range(257):
    hashmap[i] = {}

with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        values = line.strip().split(',')

def hash(item):
    current_val = 0
    for char in item:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256
    return current_val

for lens in values:
    operator = '='
    if operator in lens:
        specs = lens.split('=')
        label = specs[0]
        focal_length = int(specs[1])
        box_number = hash(label)
        hashmap[box_number][label] = focal_length
    else:
        operator = lens[-1:]
        label = lens[:-1]
        box_number = hash(label)
        if label in hashmap[box_number].keys():
            del hashmap[box_number][label]

total = 0
for box, lenses in hashmap.items():
    for position, focal_length in enumerate(lenses.values(), start=1):
        total += (box + 1) * position * focal_length

print("TOTAL: ", total)