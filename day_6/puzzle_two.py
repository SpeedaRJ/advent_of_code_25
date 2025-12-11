import time
from math import prod

start_time = time.time()

with open("./day_6/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

total = 0

nums = []
for i in reversed(range(len(lines[0]))):
    column = ''.join(line[i] for line in lines)
    if not column.strip():
        continue

    nums.append(int(column[:-1]))
    if column[-1] == "*":
        total += prod(nums)
        nums = []
    elif column[-1] == "+":
        total += sum(nums)
        nums = []
    else:
        continue

print(total)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))