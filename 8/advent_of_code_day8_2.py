def multiply(vals):
    new = 0
    for i, val in enumerate(vals):
        if i == 0:
            new = val
        else:
            new *= val
    return new


tree_map = []
all_sums = []
with open(r'C:\Users\nsa\Documents\AdventOfCode\8\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        tree_map.append([num for num in row])
current_column = 1
current_row = 1
for row in tree_map[1:-1]:
    current_row += 1
    while current_column < len(tree_map[0]) - 1:
        sums = []
        nbr_of_trees = 0
        current_tree = row[current_column]
        for tree in reversed(row[0:current_column]):
            if tree >= current_tree:
                nbr_of_trees += 1
                break
            else:
                nbr_of_trees += 1
        sums.append(nbr_of_trees)
        nbr_of_trees = 0
        for tree in row[current_column+1:]:
            if tree >= current_tree:
                nbr_of_trees += 1
                break
            else:
                nbr_of_trees += 1
        sums.append(nbr_of_trees)
        nbr_of_trees = 0
        for tree_row in reversed(tree_map[0:current_row-1]):
            if tree_row[current_column] >= current_tree:
                nbr_of_trees += 1
                break
            else:
                nbr_of_trees += 1
        sums.append(nbr_of_trees)
        nbr_of_trees = 0
        for tree_row in tree_map[current_row:]:
            if tree_row[current_column] >= current_tree:
                nbr_of_trees += 1
                break
            else:
                nbr_of_trees += 1
        sums.append(nbr_of_trees)
        all_sums.append(sums)
        nbr_of_trees = 0
        current_column += 1
    current_column = 1
print(max(multiply(v) for v in all_sums))

