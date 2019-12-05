import numpy as np
import random

n = 2
k = 3

M = np.zeros((k, n+1))
c = [random.randint(0, n+1) for i in range(k)]
c = [0.25, 0.5, 0]

sums = np.zeros(n+1)

for i in range(k-1, -1, -1):
    for j in range(n, -1, -1):
        r = 0
        if i == k-1:
            r = j*((j+1)/(n+1)) + (1/(n+1))*((n*(n+1)-j*(j+1))/2) - c[i]
        else:
            r = M[i+1, j]*((j+1)/(n+1)) + (1/(n+1))*sums[j] - c[i]
            
        M[i, j] = max(j, r)
        
        if j == n:
            sums[j] = 0
        else:
            sums[j] = sums[j+1] + M[i, j+1]
                
print("Optimal expected value: " + str(M[0, 0]))