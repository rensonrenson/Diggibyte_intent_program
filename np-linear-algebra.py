import numpy as np

N = int(input())

A = np.array([list(map(float, input().split())) for i in range(N)])

print(np.round(np.linalg.det(A), 2))
