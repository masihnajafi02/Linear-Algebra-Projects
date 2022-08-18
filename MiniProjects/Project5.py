import numpy as np


def eig_vals(A: np.matrix, iter: int) -> np.array:
    for _ in range(iter):
        q, r = np.linalg.qr(A)
        A = np.dot(r, q)
    return A

A = np.array(np.matrix(input(), dtype=int))
A = eig_vals(A, 1000)
the_list = []
i=0
j=0
while i < len(A):
    the_list.append(A[i][j])
    i += 1
    j += 1

A=the_list
for element in sorted((A), reverse=True):
    print(format(element, '.2f'), end=' ')
