elfs = {}
with open(r'C:\Users\nsa\Documents\AdventOfCode\1\items.txt', 'r', encoding='utf-8') as file:
    cals = 0
    i = 0
    for row in file:
        if row == '\n':
            cals = 0
            i += 1
        else:
            cals += int(row)
            elfs[i] = cals

print(max([i for i in elfs.values()]))
