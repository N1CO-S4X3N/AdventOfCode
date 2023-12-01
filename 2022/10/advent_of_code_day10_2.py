x = 1
cycles = 0
integer = 0
total_cycles = 0
total_sum = 0
signal_strength = 0
lit_pixel = '#'
dark_pixel = '.'
current_row = ''
pixel_column = 0
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
            if pixel_column in range(x-1, x+2):
                current_row += lit_pixel
            else:
                current_row += dark_pixel
            if pixel_column < 39:
                pixel_column += 1
            else:
                pixel_column = 0
            if total_cycles % 40 == 0:
                signal_strength = x * total_cycles
                total_sum += signal_strength
                print(current_row)
                current_row = ''
        x += integer

print('total_sum: ', total_sum)
print('total_cycles: ', total_cycles)
print('signal_strength: ', signal_strength)
print('x: ', x)
