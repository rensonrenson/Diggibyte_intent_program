import numpy as np

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr  = np.array(arr, dtype=float)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))
