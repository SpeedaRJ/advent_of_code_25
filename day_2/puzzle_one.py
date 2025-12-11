import time

start_time = time.time()

with open("./day_2/input.txt") as fs:
    lines = fs.read()

# SOLUTION 

sum = 0

list = lines.split(",")

for entry in list:
    entry_split = entry.split("-")
    start = int(entry_split[0])
    end = int(entry_split[1])

    for number in range(start, end + 1):
        number_str = str(number)
        number_len = len(number_str)
        if number_len % 2 == 0 and number_str[0:number_len // 2] == number_str[number_len // 2:]:
            sum += number

print(sum)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))