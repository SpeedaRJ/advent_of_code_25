import time
from functools import cache

start_time = time.time()

with open("./day_11/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

graph = {}
for line in lines:
    node, neighbors_str = line.split(': ')
    neighbors = neighbors_str.split(' ')
    graph[node] = neighbors

@cache
def count_paths(current_node):
    if current_node == 'out':
        return 1

    total_paths = 0
    if current_node in graph:
        for neighbor in graph[current_node]:
            total_paths += count_paths(neighbor)

    return total_paths

num_paths = count_paths('you')
print(num_paths)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))