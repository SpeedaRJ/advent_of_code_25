import time

start_time = time.time()

with open("./day_9/input.txt") as fs:
    lines = fs.read().splitlines()

# SOLUTION 

points = [list(map(int, line.split(','))) for line in lines]

n = len(points)

def area(node_1, node_2):
    width = abs(node_1[0] - node_2[0]) + 1
    height = abs(node_1[1] - node_2[1]) + 1
    return width * height

edges = []
sizes = []
for i in range(n):
    edges.append(sorted((points[i], points[i-1])))
    for j in range(i+1, n):
        c1, c2 = sorted((points[i], points[j]))
        sizes.append((area(points[i], points[j]), c1, c2))

edges.sort(reverse=True, key=lambda e: area(e[0], e[1]))
sizes.sort(reverse=True)

for size, (x1, y1), (x2, y2) in sizes:
    y1, y2 = sorted((y1, y2))
    if not any(
        (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
        for (x3, y3), (x4, y4) in edges
    ):
        print(size)
        break

# SOLUTION 

print("--- %s seconds ---" % (time.time() - start_time))