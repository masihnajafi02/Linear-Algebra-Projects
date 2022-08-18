import numpy as np

first_line = input().split()
k = int(first_line[0])
m = int(first_line[1])
n = int(first_line[2])

points = []
for i in range(m):
    points.append(np.array(input().split(), dtype=float))

votes = np.array(input().split(), dtype=int)

not_decided = []
for j in range(n):
    not_decided.append(np.array(input().split(), dtype=float))

points = np.array(points, dtype=float)
not_decided = np.array(not_decided, dtype=float)

for element in not_decided:
    data = np.linalg.norm(element - points, axis=1)
    decided = np.argpartition(data, k)[:k]
    final = votes[decided]
    print(np.argmax(np.bincount(final)), end=' ')
