import os
import sys


combinations = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        combinations.append([])
        for char in line:
            if char.isnumeric():
                combinations[i].append(char)

result = 0
for number in combinations:
    if len(number) == 1:
        result += int(number[0] + number[0])
    else:
        result += int(number[0] + number[-1])

print("result: ", result)