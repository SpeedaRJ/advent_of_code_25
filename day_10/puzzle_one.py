import time
from collections import deque

start_time = time.time()

with open("./day_10/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

lines = [line.strip() for line in lines]

targets = [line.split(" ")[0] for line in lines]
initial_states = [["0" if c == '.' else "1" for c in target[1:-1]] for target in targets]

buttons = [
    " ".join(line.split(" ")[1:-1]) for line in lines
]

buttons = [
    [tuple(int(x) for x in b[1:-1].split(',')) for b in button_set.split()]
    for button_set in buttons
]

total = 0

def process_row(start, button_masks):
    seen = set()
    queue = deque([(start, 0)])
    while queue:
        state, steps = queue.popleft()
        if state == 0:
            return steps
        if state in seen:
            continue
        seen.add(state)
        for mask in button_masks:
            queue.append((state ^ mask, steps + 1))

for state, button_set in zip(initial_states, buttons):
    start = int("".join(state[::-1]), 2)
    button_masks = [sum(1 << idx for idx in button) for button in button_set]
    total += process_row(start, button_masks)
    
print(total)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))