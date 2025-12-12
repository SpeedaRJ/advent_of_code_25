import time
import numpy as np

start_time = time.time()

with open("./day_12/input.txt") as fs:
    lines = fs.read().split("\n\n")

# SOLUTION

def parse_region(region):
    dimensions_raw, count_raw = region.split(":")
    dimensions = (int(dimensions_raw.split("x")[0]), int(dimensions_raw.split("x")[1]))
    count = [int(num) for num in count_raw.strip().split()]
    return dimensions, count


def check_region(presents, region):
    (width, height), count = region
    total = sum(p * c for p, c in zip(presents, count))
    if total > width * height:
        return -1
    if (width // 3) * (height // 3) >= sum(count):
        return 1
    return 0


tasks = [parse_region(region) for region in lines[-1].split("\n")]
presents = [line.count("#") for line in lines[:-1]]

count = [check_region(presents, task) for task in tasks]

print(count.count(1))

# SOLUTION

print("--- %s seconds ---" % (time.time() - start_time))
