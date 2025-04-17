import numpy as np

#Rahe aval
def Cart1(arr):
    return np.array(np.meshgrid(*arr)).T.reshape(-1,len(arr))

#Rahe dovvom
def Cart2(arr):
    arr = [np.asarray(a) for a in arr]
    shape = (len(x) for x in arr)

    i = np.indices(shape, dtype=int)
    i = i.reshape(len(arr), -1).T

    for n, arr2 in enumerate(arr):
        i[:, n] = arr[n][i[:, n]]

    return i

a = [[1,2,3], [4,5,6], [7,8,9],[10,11,12]]
print(Cart1(a))
print(Cart2(a))
