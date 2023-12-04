import os
import sys


def count_value(occurrance):
    if occurrance == 1:
        return occurrance
    value = 1
    for i in range(1, occurrance):
        value = value * 2
    return value

total = 0
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        numbers = line.strip().split(': ')[1]
        numbers = numbers.split(' | ')
        winning =  [int(n) for n in numbers[0].split(' ') if n.isdigit()]
        own = [int(n) for n in numbers[1].split(' ') if n.isdigit()]
        occurrance = sum(element in own for element in winning)
        if occurrance:
            total += count_value(occurrance)


print("Total: ", total)
