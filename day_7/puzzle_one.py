import time

start_time = time.time()

with open("./day_7/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

lines = [list(line.strip()) for line in lines]

output = lines.copy()

sum = 0 

for line_idx, line in enumerate(lines[1:]):
    for loc_idx, location in enumerate(line):
        if (lines[line_idx][loc_idx] == "S" or lines[line_idx][loc_idx] == "|") and location != "^":
            output[line_idx + 1][loc_idx] = "|"    
        if location == "^" and lines[line_idx][loc_idx] == "|":
            sum += 1
            output[line_idx + 1][loc_idx - 1] = "|"
            output[line_idx + 1][loc_idx + 1] = "|"

print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))