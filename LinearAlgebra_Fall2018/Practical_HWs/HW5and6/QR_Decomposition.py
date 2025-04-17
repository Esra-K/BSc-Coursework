import numpy as np
import random

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A


def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


A = []
n = int(input())
for i in range(n):
    # k = []
    # for j in range(n):
    #     rand = random.uniform(0.0, 1000000.0)
    #     k.append(rand)
    k = list(map(float, input().split(" ")))
    A.append(k)
#print(A)
a = np.array(A, dtype=float)
q, r = qr(a)
for i in range(len(q)):
    for j in range(len(q[i])):
        if j == len(q[i]) - 1:
            print(q[i][j], end="\n")
        else:
            print(q[i][j], end=" ")

for i in range(len(r)):
    for j in range(len(r[i])):
        if j == len(r[i]) - 1:
            print(r[i][j], end="\n")
        else:
            print(r[i][j], end=" ")
# test = np.matmul(np.matrix(q), np.matrix(r)).tolist()
# print(test)
#
# err = 0
# for i in range(n):
#     for j in range(n):
#         err += abs(A[i][j] - test[i][j])
# print(err)