import time
import heapq

start_time = time.time()

with open("./day_3/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

sum = 0

for line in lines:
    line = line.strip()
    leading_number = heapq.nlargest(2, line)
    candidate = leading_number[0]
    candidate_postion = line.find(candidate)
    if candidate_postion + 1 == len(line):
        candidate = leading_number[1]
        candidate_postion = line.find(candidate)
    following_number = max(line[candidate_postion + 1:])
    sum += int(f"{candidate}{following_number}")

print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))