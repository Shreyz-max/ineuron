import numpy as np

x = np.array([1, 2, 3, 4, 5])
n = 3
print(np.vander(x, n))
print(x**n)
arr = []
newArray = np.column_stack([x**(n-i-1) for i in range(n)])


def moving_window(seq, k):
    final = []
    for i in range(len(seq)-k+1):
        final.append(np.round(np.mean([seq[i+m] for m in range(k)]), 2))
    return final


print(moving_window([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150], 3))