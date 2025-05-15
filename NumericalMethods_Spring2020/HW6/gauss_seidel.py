import numpy as np
from pandas import DataFrame
from math import fabs


# Reads 15 comma-separated real values. Values 9 to 1 would be the 3*3 matrix (A)
# Values 10 to 12 would be the b vector in Ax = b
# Values 13 to 15 would be the initial x values
l = list(map(float, input().split(",")))
if len(l) != 15:
    raise Exception("Input length was not equal to 15")
a, b, initials = np.reshape(np.array(l[:9]), (3, 3)), l[9:12], l[12:]
# print(a)
# print(b)
# print(initials)

# Swap rows in case a diagonal is zero
for i in range(len(a)):
    if a[i][i] == 0.:
        for j in range(i+1, len(a)):
            if a[j][i] != 0:
                a[[i, j]] = a[[j, i]]
                b[i], b[j] = b[j], b[i]
                # print(a)
                # print(b)
                break

# Estimates the x vector using Gauss-Seidel method
steps = 3
x = np.array(initials)
for s in range(1, steps + 1):
    x_new = np.array([0. for i in range(len(initials))])
    for i in range(a.shape[0]):
        t1 = np.dot(x_new[:i], a[i][:i])
        t2 = np.dot(x[i + 1:], a[i][i + 1:])
        x_new[i] = (b[i] - t1 - t2) / a[i][i]
    x = x_new
    print(str(s) + 'th iteration. x=' + str(x))

# Print out the results
real_x = np.linalg.solve(a, b)
error = np.array(list(map(fabs, real_x - x)))
result = DataFrame(np.transpose([x, real_x, error]), columns=["estimated x", "real x", "error"])
print(result)
