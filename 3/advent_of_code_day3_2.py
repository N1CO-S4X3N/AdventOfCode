import string

priority_sum = 0
uppercase_prio_start = len(string.ascii_lowercase)
group_items = []
with open(r'C:\Users\nsa\Documents\AdventOfCode\3\items2.txt', 'r', encoding='utf-8') as file:
    i = 1
    for row in file:
        row = row.strip()
        group_items.append(row)
        print(group_items)
        if i % 3 == 0:
            for item in set(group_items[0]):
                if item in group_items[1] and item in group_items[2]:
                    if item.isupper():
                        priority_sum += string.ascii_uppercase.index(item) + 1 + uppercase_prio_start
                    else:
                        priority_sum += string.ascii_lowercase.index(item) + 1
            group_items = []
        i += 1
print(priority_sum)

