import time
from functools import cache

start_time = time.time()

with open("./day_11/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

graph = {}
for line in lines:
    node, neighbors_str = line.split(': ')
    graph[node] = neighbors_str.split(' ')


path_in_progress = set()

@cache
def count_simple_paths(node, has_dac, has_fft):
    if node in path_in_progress:
        return 0

    if node == 'out':
        return 1 if has_dac and has_fft else 0

    path_in_progress.add(node)

    total = 0
    if node in graph:
        for neighbor in graph[node]:
            next_has_dac = has_dac or (neighbor == 'dac')
            next_has_fft = has_fft or (neighbor == 'fft')
            
            total += count_simple_paths(neighbor, next_has_dac, next_has_fft)
    
    path_in_progress.remove(node)
    return total

start_node = 'svr'
initial_has_dac = (start_node == 'dac')
initial_has_fft = (start_node == 'fft')
    
result = count_simple_paths(start_node, initial_has_dac, initial_has_fft)

print(result)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))