import sys
import numpy as np
import math as m
  
def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])



N = int(input())
vector = []
for i in range(N):
    temp=np.array(input().split(), dtype=float)
    vector.append(temp)
vector = np.array(vector)

angle = np.array(input().split(), dtype=float)

formatter = "{:.1f}".format
np.set_printoptions(formatter={'float_kind': formatter}, threshold=sys.maxsize)
vector=np.array(np.dot(Rz(angle[2]) * Ry(angle[1]) * Rx(angle[0]), vector.T)).T
print(np.round(vector, decimals=1))
