import time
import numpy as np

start_time = time.time()

with open("./day_3/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION

def max_in_range(sequence, lights, pos, start, stop=None):
    sequence = sequence[start:stop]
    new_index = 0
    for i, light in enumerate(sequence):
        if int(light) > int(sequence[new_index]):
            new_index = i
    lights[pos] = new_index + start
    return lights

sum = 0

for line in lines:
    line = line.strip()
    lights = np.zeros(12, dtype=np.int16)
    lights = max_in_range(line, lights, 0, 0, -11)
    lights = max_in_range(line, lights, 1, lights[0] + 1, -10)
    lights = max_in_range(line, lights, 2, lights[1] + 1, -9)
    lights = max_in_range(line, lights, 3, lights[2] + 1, -8)
    lights = max_in_range(line, lights, 4, lights[3] + 1, -7)
    lights = max_in_range(line, lights, 5, lights[4] + 1, -6)
    lights = max_in_range(line, lights, 6, lights[5] + 1, -5)
    lights = max_in_range(line, lights, 7, lights[6] + 1, -4)
    lights = max_in_range(line, lights, 8, lights[7] + 1, -3)
    lights = max_in_range(line, lights, 9, lights[8] + 1, -2)
    lights = max_in_range(line, lights, 10, lights[9] + 1, -1)
    lights = max_in_range(line, lights, 11, lights[10] + 1)
    batteries = np.array(list(line))
    sum += int(''.join(batteries[lights]))

print(sum)

# SOLUTION

print("--- %s seconds ---" % (time.time() - start_time))
