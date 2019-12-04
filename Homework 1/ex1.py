import numpy as np

n = 2
k = 3

M = np.zeros((k+1, n+1))
c = [0, 0.25, 0.5, 0]

def sum_range(t):
    res = 0
    for i in range(1, t+1):
        res += c[i]
    return res

def find_imax(b):
    imax = 0
    for i in range(len(b)):
        if b[i] >= imax:
            imax = i
        else:
            return imax
    return imax

for i in range(1, k+1):
    for j in range(n+1):
        M[i, j] = j*(j+1)/(n+1) + (n*(n+1) - (j+2)*(j+1))/(2*(n+1)) - sum_range(i)

print(M)

res = 0
for i in range(1, k+1):
    imax = find_imax(M[i])
    imax2 = find_imax(M[i-1])
    for j in range(imax+1, n+1):
        res += M[i, j]
    res *= pow(imax2, i-1)/pow(n+1, i)
    res += res
print(res)

