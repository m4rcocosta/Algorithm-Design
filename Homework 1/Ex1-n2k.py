import numpy as np
import random

n = 2
k = 3

M = np.zeros((k,n+1))

c = [1 for i in range(k)]
c = [0.25, 0.5, 0]

for i in range(k-1, -1, -1):
    for j in range(n, -1, -1):
        r = 0
        mysum = 0
        if i == k-1:
            r += j*(j+1)/(n+1)
            for x in range(j+1, n+1):
                mysum += x
            r += mysum/(n+1)
        else:
            r += M[i+1, j]*(j+1)/(n+1)
            for x in range(j+1, n+1):
                mysum += M[i+1, x]
            r += mysum/(n+1)
        r -= c[i]
        M[i][j] = max(j, r)

print("Optimal expected value: " + str(M[0][0]))