import time
import numpy as np
import re

start_time = time.time()

with open("./day_6/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

lines = np.array([re.split(r"\ +", line.strip()) for line in lines]).transpose()

sum = 0 

for problem in lines:
    algo = problem[-1]
    if algo == "+":
        sum += int(problem[0]) + int(problem[1]) + int(problem[2]) + int(problem[3])
    elif algo == "*":
        sum += int(problem[0]) * int(problem[1]) * int(problem[2]) * int(problem[3])
    else:
        continue

print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))