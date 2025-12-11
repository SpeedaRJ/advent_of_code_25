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
    distance = int(line[1:])

    if direction == "R":
        for _ in range(distance):
            dial = (dial + 1) % 100
            if dial == 0:
                counter += 1
    elif direction == "L":
        for _ in range(distance):
            dial = (dial - 1 + 100) % 100
            if dial == 0:
                counter += 1

print(counter)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))