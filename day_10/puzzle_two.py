import time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

start_time = time.time()

with open("./day_10/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

lines = [line.strip() for line in lines]

targets = [line.split(" ")[-1] for line in lines]
voltages = [
     [int(x) for x in voltage_part[1:-1].split(',')] for voltage_part in targets
]

buttons = [
    " ".join(line.split(" ")[1:-1]) for line in lines
]

buttons = [
    [tuple(int(x) for x in b[1:-1].split(',')) for b in button_set.split()]
    for button_set in buttons
]

total = 0

for voltage, button_set in zip(voltages, buttons):
    n_buttons = len(button_set)
    n_outputs = len(voltage)

    A = np.zeros((n_outputs, n_buttons))
    for i, button in enumerate(button_set):
        for idx in button:
            if idx < n_outputs:
                A[idx, i] = 1

    b = np.array(voltage)

    c = np.ones(n_buttons) 
    constraints = LinearConstraint(A, b, b) 
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)

    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

    total += int(round(result.fun))

print(total)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))