import os
import sys


with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        values = line.strip().split(',')

total = 0
for item in values:
    current_val = 0
    for char in item:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256
    total += current_val

print(total)
