import numpy as np

first_line=input().split()
N=int(first_line[0])
M=int(first_line[1])
K=int(first_line[2])

vectors = np.vstack([np.transpose(np.array([input().split() for i in range(M)], dtype=np.float64)), np.ones(M)])

if M > N:
    for i in range(K):
        print("YES")
    exit()

print()
try:
    inverse=np.array(np.matrix(vectors[:np.shape(vectors)[1]]).I)
except:
    for i in range(K):
        print("YES")
    exit()


for i in range(K):
    point=np.array(input().split() + [1], dtype=np.float64)
    x=np.dot(inverse,point[:np.shape(vectors)[1]])
    if np.all(np.abs(np.dot(vectors, x) - point) < 10**(-8)):
        print("YES")
    else:
        print("NO")
  




