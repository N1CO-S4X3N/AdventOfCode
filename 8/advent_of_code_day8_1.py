total_sum = 0
tree_map = []
with open(r'C:\Users\nsa\Documents\AdventOfCode\8\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        tree_map.append([num for num in row])
width = len(tree_map[0])
height = len(tree_map)
total_sum = (2 * width) + (2 * (height - 2))
current_column = 1
current_row = 1
for row in tree_map[1:-1]:
    current_row += 1
    while current_column < width - 1:
        current_tree = row[current_column]
        if (current_tree > max(tree for tree in row[0:current_column])
                or current_tree > max(tree for tree in row[current_column+1:])):
            total_sum += 1
        elif (current_tree > max(tree_row[current_column] for tree_row in tree_map[0:current_row-1])
              or current_tree > max(tree_row[current_column] for tree_row in tree_map[current_row:])):
            total_sum += 1
        current_column += 1
    current_column = 1
print('tree_map: ', tree_map)
print('total_sum: ', total_sum)
