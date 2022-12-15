coordinates_list = []
rock_coordinates = set()
max_x = 0
min_x = 10000
max_y = 0
with open(r'.\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        coordinates = row.split(' -> ')
        for xy in coordinates:
            x, y = xy.split(',')
            if int(x) > max_x:
                max_x = int(x)
            elif int(x) < min_x:
                min_x = int(x)
            if int(y) > max_y:
                max_y = int(y)
            coordinates_list.append((int(x), int(y)))
        for nbr, coord in enumerate(coordinates_list):
            if nbr + 1 > len(coordinates_list) - 1:
                break
            this_x, next_x = coordinates_list[nbr][0], coordinates_list[nbr+1][0]
            this_y, next_y = coordinates_list[nbr][1], coordinates_list[nbr+1][1]
            if this_x < next_x:
                for i in range(this_x, next_x+1):
                    rock_coordinates.add((i, this_y))
            elif this_x > next_x:
                for i in range(this_x, next_x-1, -1):
                    rock_coordinates.add((i, this_y))
            elif this_y < next_y:
                for i in range(this_y, next_y+1):
                    rock_coordinates.add((this_x, i))
            elif this_y > next_y:
                for i in range(this_y, next_y-1, -1):
                    rock_coordinates.add((this_x, i))
        coordinates_list = []
floor_y = 2 + max_y
sand_x = 500
sand_y = 0
all_resting = False
resting_count = 0
while not all_resting:
    # if (sand_x + 1 > max_x and sand_y + 1 > floor_y) or (sand_x - 1 < min_x and sand_y + 1 > floor_y):
    #     all_resting = True
    if not (sand_x, sand_y+1) in rock_coordinates and sand_y+1 != floor_y:
        sand_y += 1
    elif not (sand_x-1, sand_y+1) in rock_coordinates and sand_y+1 != floor_y:
        sand_x -= 1
        sand_y += 1
    elif not (sand_x+1, sand_y+1) in rock_coordinates and sand_y+1 != floor_y:
        sand_x += 1
        sand_y += 1
    else:
        rock_coordinates.add((sand_x, sand_y))
        sand_x = 500
        sand_y = 0
        if (sand_x, sand_y) in rock_coordinates:
            all_resting = True
        resting_count += 1
print("resting: ", resting_count)
