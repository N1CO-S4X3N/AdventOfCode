import matplotlib.pyplot as plt
import re


class Sensor:
    def __init__(self, closest_beacon, coordinate, manhattan_distance):
        self.closest_beacon = closest_beacon
        self.coordinate = coordinate
        self.manhattan_distance = manhattan_distance


def get_x_and_y(text):
    x_text, y_text = re.findall(r'x=-?\d+', text)[0], re.findall(r'y=-?\d+', text)[0]
    _x, _y = int(x_text.replace('x=', '')), int(y_text.replace('y=', ''))
    return _x, _y


sensors = []
no_beacon_space_in_row = set()
location_of_beacons = set()
location_of_sensors = set()
# For plotting the squares around each sensor
square_searches = {}
y_row_to_calculate = 2000000
with open(r'.\items2.txt', 'r', encoding='utf-8') as file:
    for i, row in enumerate(file):
        row = row.strip()
        print(row)
        row = row.split(': ')
        sensor_text, beacon_text = row[0], row[1]
        sensor_x, sensor_y = get_x_and_y(sensor_text)
        beacon_x, beacon_y = get_x_and_y(beacon_text)
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensor = Sensor((beacon_x, beacon_y), (sensor_x, sensor_y), distance)
        sensors.append(sensor)
        location_of_beacons.add((beacon_x, beacon_y))
        location_of_sensors.add((sensor_x, sensor_y))
        # Plotting stuff
        point_right = (sensor_x + distance, sensor_y)
        point_down = (sensor_x, sensor_y + distance)
        point_left = (sensor_x - distance, sensor_y)
        point_up = (sensor_x, sensor_y - distance)
        square_searches[i] = [point_right, point_down, point_left, point_up, point_right, (sensor_x, sensor_y)]
for sensor in sensors:
    location = sensor.coordinate
    sensor_distance = sensor.manhattan_distance
    distance_to_row = abs(location[1] - y_row_to_calculate)
    distance = abs(sensor_distance - distance_to_row)
    if distance_to_row <= sensor_distance:
        for x in range(location[0] - distance, location[0] + distance + 1):
            no_beacon_space_in_row.add(x)
# Don't calculate beacons or sensors as spaces for the row
for loc_x, loc_y in location_of_beacons:
    if loc_y == y_row_to_calculate:
        no_beacon_space_in_row.remove(loc_x)
for loc_x, loc_y in location_of_sensors:
    if loc_y == y_row_to_calculate:
        no_beacon_space_in_row.remove(loc_x)
print(len(no_beacon_space_in_row))

# Plot the beacons, sensors and their scan squares
row = []
x_left, x_right = min(no_beacon_space_in_row), max(no_beacon_space_in_row)
plt.rcdefaults()
fig = plt.figure()
ax = fig.gca()
plt.gca().invert_yaxis()
plt.scatter(*zip(*location_of_beacons))
plt.scatter(*zip(*location_of_sensors), color='green')
for x_y_list in square_searches.values():
    plt.plot(*zip(*x_y_list))
line = [(x_left, y_row_to_calculate), (x_right, y_row_to_calculate)]
plt.plot(*zip(*line), color='purple', alpha=0.5)
plt.grid()
plt.show()
