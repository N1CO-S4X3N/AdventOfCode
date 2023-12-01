x = 1
cycles = 0
integer = 0
total_cycles = 0
total_sum = 0
signal_strength = 0
with open(r'.\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        if row == 'noop':
            cycles = 1
            integer = 0
        elif row.startswith('addx'):
            cycles = 2
            integer = int(row.split(' ')[-1])
        for c in range(0, cycles):
            total_cycles += 1
            if total_cycles == 20 or (total_cycles - 20) % 40 == 0:
                signal_strength = x * total_cycles
                total_sum += signal_strength
                print('TOTAL: ', total_sum)
                print('SIGNAL: ', signal_strength)
                print('X: ', x)
        x += integer

print('total_sum: ', total_sum)
print('total_cycles: ', total_cycles)
print('signal_strength: ', signal_strength)
print('x: ', x)
