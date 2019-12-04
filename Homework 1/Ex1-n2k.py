import numpy as np
import random

n = 2
k = 3

M = np.zeros((k,n+1))

costs = [1 for i in range(k)]
costs = [0.25, 0.5, 0]

for i in range(k-1, -1, -1):
    expected = 0
    for j in range(0, n+1):
        expected = 0
        for x in range(0, n+1):
            v_max = max(j, x)
            if i == k-1:
                expected += v_max/(n+1)
            else:
                expected += (M[i+1][v_max])/(n+1)
        expected -= costs[i]
        M[i][j] = max(j, expected)

print("Optimal expected value: " + str(M[0][0]))