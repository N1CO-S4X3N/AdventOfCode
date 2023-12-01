amount = 0
with open(r'C:\Users\nsa\Documents\AdventOfCode\4\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        range1, range2 = row.split(',')
        range1_1, range1_2 = range1.split('-')
        range1 = list(range(int(range1_1), int(range1_2) + 1))
        range2_1, range2_2 = range2.split('-')
        range2 = list(range(int(range2_1), int(range2_2) + 1))
        if all(v in range2 for v in range1) or all(v in range1 for v in range2):
            amount += 1
print(amount)

