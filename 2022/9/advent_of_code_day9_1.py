head_coord = (1000, 1000)
previous_head_coord = (1000, 1000)
tail_coord = (1000, 1000)
visited_coords = set()
with open(r'C:\Users\nsa\Documents\AdventOfCode\9\items2.txt', 'r', encoding='utf-8') as file:
    visited_coords.add(tail_coord)  # Add starting coord
    for row in file:
        row = row.strip()
        direction, steps = row.split(' ')
        for step in range(0, int(steps)):
            previous_head_coord = head_coord
            if direction == 'R':
                head_coord = (head_coord[0] + 1, head_coord[1])
            elif direction == 'U':
                head_coord = (head_coord[0], head_coord[1] + 1)
            elif direction == 'L':
                head_coord = (head_coord[0] - 1, head_coord[1])
            else:
                head_coord = (head_coord[0], head_coord[1] - 1)
            if ((head_coord[0] == tail_coord[0] + 2 or head_coord[0] == tail_coord[0] - 2)
                    or (head_coord[1] == tail_coord[1] + 2 or head_coord[1] == tail_coord[1] - 2)):
                tail_coord = (previous_head_coord[0], previous_head_coord[1])
                visited_coords.add(tail_coord)
print('total visited at least once: ', len(visited_coords))

