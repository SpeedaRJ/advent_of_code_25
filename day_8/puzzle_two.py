import time
import numpy as np

start_time = time.time()

with open("./day_8/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

points = [list(map(int, line.split(','))) for line in lines]

n = len(points)

distances = [
    (np.linalg.norm(np.array(points[i]) - np.array(points[j])), {i,j}) for i in range(n-1) for j in range(i + 1, n)
]

circuits = []

i = 0
j = 0

for _, connection in sorted(distances):
    overlap = []
    for i, circuit in enumerate(circuits):
        if circuit & connection:
            overlap.append(i)

    if not overlap:
        circuits.append(connection)
    elif len(overlap) == 1:
        circuits[overlap[0]] |= connection
    else:
        circuits[overlap[0]] |= circuits.pop(overlap[1])

    if len(circuits[0]) == n:
        i, j = connection
        break

print(points[i][0] * points[j][0])

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))