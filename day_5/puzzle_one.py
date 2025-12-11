import time
import numpy as np

start_time = time.time()

with open("./day_5/input.txt") as fs:
    lines = fs.read()

# SOLUTION 

fresh_ranges, ids = lines.split("\n\n")

fresh_count = 0

ranges = []

for fresh_range in fresh_ranges.split("\n"):
    fresh_range = fresh_range.strip()
    start, end = fresh_range.split("-")
    ranges.append((int(start), int(end)))

ranges = np.array(ranges)

for id in ids.split('\n'):
    id = int(id.strip())
    lower_bound = ranges[:, 0] <= id
    upper_bound = ranges[:, 1] >= id
    if (lower_bound == upper_bound).any():
        fresh_count += 1

print(fresh_count)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))