import time

start_time = time.time()

with open("./day_2/input.txt") as fs:
    lines = fs.read()

# SOLUTION 

import re

pattern = re.compile(r"^(.+?)\1+$")

sum = 0

list = lines.split(",")

for entry in list:
    entry_split = entry.split("-")
    start = int(entry_split[0])
    end = int(entry_split[1])

    for number in range(start, end + 1):
        number_str = str(number)
        match = pattern.fullmatch(number_str)
        if match is not None:
            sum += number
        
print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))