structure = {}
current_dir = ''
path = ""
with open(r'I:\Documents\PythonPrograms\AdventOfCode\7\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        if '/' in row:
            current_dir = row.split(' ')[-1] + '|'
            structure[current_dir] = []
            path = current_dir
        elif row == '$ ls':
            continue
        elif row.startswith('dir'):
            structure[path].append(path + row.split(' ')[-1] + '|')
        elif row.startswith('$ cd'):
            if '..' in row:
                path = path[0:-len(current_dir)]
                current_dir = path.split('|')[-2] + '|'
                continue
            current_dir = row.split(' ')[-1] + '|'
            path = path + current_dir
            structure[path] = []
        else:
            structure[path].append(row)
dir_sizes = {}
for path, contents in structure.items():
    sums = []
    for c in contents:
        if any(char.isdigit() for char in c):
            sums.append(int(c.split(' ')[0]))
    dir_sizes[path] = sum(sums)
for path, contents in reversed(structure.items()):
    sums = []
    for c in contents:
        if '/' in c:
            sums.append(dir_sizes[c])
    dir_sizes[path] += sum(sums)
total_sum = 0
for size in dir_sizes.values():
    if size <= 100000:
        total_sum += size
print('total_sum: ', total_sum)
