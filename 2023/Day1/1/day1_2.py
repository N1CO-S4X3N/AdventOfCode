import os
import re
import sys


words_to_numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
combinations = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        combinations.append([])
        expression = r"(?=(\d|" + "|".join(words_to_numbers.keys()) + "))"
        findall = re.findall(expression, line)
        for num in findall:
            if not num.isnumeric():
                num = words_to_numbers.get(num, 0)
            combinations[i].append(num)

result = 0
for number in combinations:
    if len(number) == 1:
        result += int(number[0] + number[0])
    else:
        result += int(number[0] + number[-1])

print("result: ", result)