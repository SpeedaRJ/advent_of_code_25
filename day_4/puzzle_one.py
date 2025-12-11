import time
import numpy as np

start_time = time.time()

with open("./day_4/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

input = []

for line in lines:
    line = list(line.strip())
    input.append(line)

input = np.array(input)
output = np.zeros_like(input)

X, Y = input.shape

for x in range(X):
    for y in range(Y):
        current_tile = input[x,y]
        if current_tile == "@":
            neighborhood = input[max(0, x - 1):min(X, x + 2), max(0, y - 1):min(Y, y + 2)]
            if (neighborhood == "@").sum() <= 4:
                output[x,y] = "."
            else:
                output[x,y] = "@"
        else:
            output[x,y] = "."

starting_rolls = (input == "@").sum()
ending_rolls = (output == "@").sum()

print(starting_rolls - ending_rolls)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))