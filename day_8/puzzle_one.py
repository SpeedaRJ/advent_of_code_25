import time
import numpy as np

start_time = time.time()

with open("./day_8/input.txt") as fs:
    lines = fs.readlines()

# SOLUTION 

points = np.array([np.array(line.strip().split(","), dtype=np.int64) for line in lines])

num_points = points.shape[0]
distance_matrix = np.zeros((num_points, num_points))

for i in range(num_points):
    for j in range(num_points):
        if i >= j:
                distance_matrix[i, j] = np.inf
        else:
            distance_matrix[i, j] = np.linalg.norm(points[i] - points[j])

flattened_indices = np.argsort(distance_matrix.flatten())[:1000]
rows, cols = np.unravel_index(flattened_indices, distance_matrix.shape)
top_1000 = list(zip(rows, cols))

circuits = []

for pair in top_1000:
    node_1, node_2 = pair
    new_circuit = True
    for i, circuit in enumerate(circuits):
        if node_1 in circuit and node_2 not in circuit:
            circuits[i].append(node_2)
            new_circuit = False
        elif node_2 in circuit and node_1 not in circuit:
            circuits[i].append(node_1)
            new_circuit = False
        elif node_1 in circuit and node_2 in circuit:
            new_circuit = False
    if new_circuit:
        circuits.append([node_1, node_2])

final_circuits = []
merged_indices = set()

for i in range(len(circuits)):
    if i in merged_indices:
        continue

    current_circuit = set(circuits[i])
    merged_indices.add(i)
    
    for j in range(i + 1, len(circuits)):
        if j in merged_indices:
            continue

        if any(element in current_circuit for element in circuits[j]):
            current_circuit.update(circuits[j])
            merged_indices.add(j)
            for k in range(len(circuits)):
                if k not in merged_indices and any(element in current_circuit for element in circuits[k]):
                    current_circuit.update(circuits[k])
                    merged_indices.add(k)

    final_circuits.append(list(current_circuit))

prod = 1

to_prod = np.sort([len(circuit) for circuit in final_circuits])[::-1][:3]

for p in to_prod:
    prod *= p

print(prod)

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))