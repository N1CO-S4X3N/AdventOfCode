import string
string.ascii_lowercase.index('b')
string.ascii_uppercase.index('B')


priority_sum = 0
uppercase_prio_start = len(string.ascii_lowercase)
with open(r'C:\Users\nsa\Documents\AdventOfCode\3\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        middle = int(len(row)/2)
        comp1 = row[:middle]
        comp2 = row[middle:]
        for item in set(comp1):
            if item in comp2:
                if item.isupper():
                    priority_sum += string.ascii_uppercase.index(item) + 1 + uppercase_prio_start
                else:
                    priority_sum += string.ascii_lowercase.index(item) + 1
print(priority_sum)

