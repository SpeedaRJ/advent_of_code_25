import time
from tqdm import tqdm
import numpy as np

start_time = time.time()

with open("./day_5/input.txt") as fs:
    lines = fs.read()

# SOLUTION 

fresh_ranges, _ = lines.split("\n\n")

sum = 0

ranges = []

for fresh_range in fresh_ranges.split("\n"):
    fresh_range = fresh_range.strip()
    start, end = fresh_range.split("-")
    ranges.append((int(start), int(end)))

ranges = np.array(ranges)

sorted_ranges = ranges[ranges[:, 0].argsort()]

merged_ranges = []
current_start, current_end = sorted_ranges[0]

for next_start, next_end in sorted_ranges[1:]:
    if next_start <= current_end + 1:
        current_end = max(current_end, next_end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = next_start, next_end

merged_ranges.append((current_start, current_end))

merged_ranges = np.array(merged_ranges)

for pair in merged_ranges:
    sum += (pair[1] - pair[0] + 1)

print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))