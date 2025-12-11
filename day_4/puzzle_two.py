import time
import numpy as np

start_time = time.time()

with open("./day_4/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

def iter_rools(input):
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
    
    return output

input = []

for line in lines:
    line = list(line.strip())
    input.append(line)

input = np.array(input)
sequence = []

first_iter = iter_rools(input)
sequence.append(first_iter)

second_iter = iter_rools(first_iter)
sequence.append(second_iter)

while (not (sequence[-1] == sequence[-2]).all()):
    new_iter = iter_rools(sequence[-1])
    sequence.append(new_iter)

starting_rolls = (input == "@").sum()
ending_rolls = (sequence[-1] == "@").sum()

print(starting_rolls - ending_rolls)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))