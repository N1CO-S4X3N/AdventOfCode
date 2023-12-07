import os
import sys
import numpy

times = []
distances = []
nbr_of_ways_to_beat = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        if i == 0:
            times = [int(t) for t in line.split(': ')[1].split()]
        else:
            distances = [int(d) for d in line.split(': ')[1].split()]

for i in range(0, len(times)):
    time = times[i]
    distance = distances[i]
    beat = 0
    for j in range(1, time):
        if j*(time-j) > distance:
            beat += 1
    nbr_of_ways_to_beat.append(beat)

print(numpy.prod(nbr_of_ways_to_beat))
