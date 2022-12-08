stacks = {}
item_list = []
nbr_of_lists = []
instruction_list = []
with open(r'C:\Users\nsa\Documents\AdventOfCode\5\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        if '[' not in row and 'from' not in row and '1' in row:
            nbr_of_lists = [int(r) for r in row.strip().split(' ') if r != '']
            continue
        row = row.replace('    ', '[-] ').replace('\n', '').replace('][', '] [').replace('  ', ' ').strip()
        if '[' in row:
            items = row.split(' ')
            item_list.append(items)
        elif 'move' in row:
            instruction_list.append(row.split(' '))
    for i in nbr_of_lists:
        stacks[i] = []
        for item in item_list:
            if item[i-1] != '' and item[i-1] != '[-]':
                stacks[i].append(item[i-1])
    for instruction in instruction_list:
        stacks[int(instruction[-1])] = stacks[int(instruction[3])][0:int(instruction[1])] + stacks[int(instruction[-1])]
        stacks[int(instruction[3])] = stacks[int(instruction[3])][int(instruction[1]):]
print('stacks: ', stacks)
code = ''.join(stack[0] for stack in stacks.values())
print(code.replace('[', '').replace(']', ''))
