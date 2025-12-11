import time
import numpy as np

start_time = time.time()

with open("./day_9/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

points = np.array([np.array(line.strip().split(","), dtype=np.int64) for line in lines])

num_points = points.shape[0]
sizes = []

for i in range(num_points - 1):
    for j in range(i + 1, num_points):
        node_1 = points[i]
        node_2 = points[j]
        width = np.abs(node_1[0] - node_2[0]) + 1
        height = np.abs(node_1[1] - node_2[1]) + 1
        sizes.append(width * height)

print(int(max(sizes)))

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))