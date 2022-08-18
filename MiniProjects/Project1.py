import numpy as np

n = int(input())
index = 0
j = 1
dictionary = {}
lines_keeper = {}
find_max = 0
for i in range(n):
    line = input().split()
    for word in line:
        if word not in dictionary:
            dictionary[word] = index
            index += 1
    lines_keeper[j] = line
    j += 1

vector_keeper = {}
for i in range(1, n + 1):
    this_line_vector = [0] * index
    for x in range(len(lines_keeper.get(i))):
        this_line_vector[dictionary.get(lines_keeper.get(i)[x])] += 1
    vector_keeper[i] = this_line_vector


for i in range(1, n + 1):
    max_ans = -1
    x_max = 0
    for x in range(1, n + 1):
        if x == i:
            continue
        list1 = vector_keeper[i]
        list2 = vector_keeper[x]
        ans = np.dot(list1, list2) / (np.linalg.norm(list1) * np.linalg.norm(list2))
        if ans > max_ans:
            max_ans = ans
            x_max = x
    print(x_max)
