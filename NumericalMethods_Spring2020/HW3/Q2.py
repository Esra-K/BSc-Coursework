import numpy as np
from matplotlib import pyplot as plt

n = 9
# All years have been subtracted by 1950 so that we won't face overflow. e.g. 1987 -> 37
xs = [5*i for i in range(10)]
ys = [2.7, 1.44, 1.58, 2.37, 2.54, 1.82, 1.42, 1.73, 1.52, 0.85]

x1 = 2
x2 = 37

r = [9 - i for i in range(10)]
a = [[x ** i for x in xs] for i in r]

determinant = np.linalg.det(np.array(a))
ba = np.array([[y for y in ys]] + a)

# for b in ba:
#     print(b)


c = [((-1.)**(n - i))/determinant for i in range(n + 1)]

for i in range(n + 1):
    mat = np.delete(ba, n + 1 - i, axis=0)

    d = np.linalg.det(np.array(mat))
    c[i] *= d

# print(c)

my_ys = np.array([np.sum(np.array([c[i]*(j**i) for i in range(len(c))])) for j in [x1, x2]])
print("Estimation for 1952:", my_ys[0])
print("Estimation for 1987:", my_ys[1])
x = np.linspace(min(xs), max(xs))
y = np.array([np.sum(np.array([c[i]*(j**i) for i in range(len(c))])) for j in x])
plt.plot(x, y)
plt.show()
