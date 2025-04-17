import numpy as np
#1 be
def find_nearest(array, value):
    array = array.ravel().flatten()
    idx = (np.abs(array - value)).argmin()
    return array[idx]

A = np.random.randint(0,5,(5,5))
B = np.random.randint(0,5,(5,5,3))

print(find_nearest(B, 2.9))

# 1 alef
A[A == np.amax(A)] = 0

#1 jim
print(A[..., None] * B)

#1 dal
A[0], A[1] = A[1], A[0]
print(A)





