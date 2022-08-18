import numpy as np

first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

cities = {}

for i in range(n):

    data = input().split()
    if cities.get(int(data[0])):

        cities.get(int(data[0])).append([float(data[1]), float(data[2])])
    else:
        cities[int(data[0])] = [[float(data[1]), float(data[2])]]

k = int(input())

for i in range(k):
    coordinates = input().split()
    data = []
    for country, coordinates_list in cities.items():
        data.append(np.linalg.norm(np.array(coordinates_list).mean(axis=0) - np.array(coordinates, dtype=float)))
    cities.get(list(cities.keys())[data.index(min(data))]).append([float(coordinates[0]), float(coordinates[1])])
    print(list(cities.keys())[data.index(min(data))], end=' ')

print()
for country, coordinates_list in dict(sorted(cities.items(), key=lambda h: h[0])).items():
    convex = []
    p = 0
    coordinates_list = sorted(coordinates_list, key=lambda h: h[0])
    print(country,end=' ')
    while True:
        convex.append(p)
        q = (p + 1) % len(coordinates_list)
        for i in range(len(coordinates_list)):
            val = (coordinates_list[i][1] - coordinates_list[p][1]) * (
                    coordinates_list[q][0] - coordinates_list[i][0]) - \
                  (coordinates_list[i][0] - coordinates_list[p][0]) * (coordinates_list[q][1] - coordinates_list[i][1])
            if val < 0:
                q = i
        p = q
        if p == 0:  break

    for i in sorted(convex):
        print("[" + "{:.2f}".format(coordinates_list[i][0]) + ", " + "{:.2f}".format(coordinates_list[i][1]) + "]",
              end=' ')
    print()
