import sys
import numpy as np

x = np.array(input().split(), dtype=np.int64)
y = np.array(input().split(), dtype=np.int64)

if len(y) < len(x):
    x, y = y, x

ans= np.zeros((len(x)+len(y)-1,len(y)), dtype=np.int64)

for i in range(len(y)):
        ans[:,i][i:i+len(x)]= x


np.set_printoptions(threshold=sys.maxsize)
print(ans@y)