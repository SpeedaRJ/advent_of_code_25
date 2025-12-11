from functools import cache
import time

start_time = time.time()

with open("./day_7/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

sample_grid = lines

start_pos = (1, sample_grid[0].index("S"))

@cache
def count_paths(row, column, count = 0):
    if row >= len(sample_grid):
        return 1

    if sample_grid[row][column] == "S" or sample_grid[row][column] == ".":
        return count + count_paths(row + 1, column, count)
    elif sample_grid[row][column] == "^":
        return count + count_paths(row + 1, column - 1, count) + count_paths(row + 1, column + 1, count)
    else:
        return count + count_paths(row + 1, column, count)

print(count_paths(start_pos[0], start_pos[1]))

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))