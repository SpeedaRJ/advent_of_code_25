import time

start_time = time.time()

with open("./day_1/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

dial = 50
counter = 0

for line in lines:
    line = line.strip()
    direction = line[0]
    distance = line[1:]

    if direction == "R":
        dial += int(distance)
    elif direction == "L":
        dial -= int(distance)

    dial = dial % 100
    if dial < 0:
        dial += 100

    if dial == 0:
        counter += 1

print(counter)

# SOLUTION

print("--- %s seconds ---" % (time.time() - start_time))