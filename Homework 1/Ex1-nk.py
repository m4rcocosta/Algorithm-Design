import numpy as np
import random

n = 2
k = 3

matrix = np.zeros((k,n+1))
c = [random.randint(0, n+1) for i in range(k)]
c = [0.25, 0.5, 0]

a = np.zeros(n+1)

for i in range(k-1, -1, -1):
    for j in range(n, -1, -1):
        nv = 0
        if i == k-1:
            nv = j*((j+1)/(n+1)) + (1/(n+1))*((n*(n+1)-j*(j+1))/2) - c[i]
        else:
            nv = matrix[i+1, j]*((j+1)/(n+1)) + (1/(n+1))*a[j] - c[i]
            
        matrix[i, j] = max(j, nv)
        
        if j == n:
            a[j] = 0
        else:
            a[j] = a[j+1] + matrix[i, j+1]
                
print(matrix[0][0])