import numpy as np
import random as rand

def isPermutation(A, B):
    C1 = A[:]
    C2 = B[:]
    C1.sort()
    C2.sort()
    return C1 == C2

r = 4
c = 5
m = [0] * (r*c)
for i in range(r * c):
    m[i] = rand.randint(1, 10)

A = np.reshape(m,(r,c))
print("original Matrix:")
print(A)

# making sure B is indeed a permutation of A's rows and columns
per = np.random.permutation(r)
B =[[0] * c] * r
for p in range(len((per))):
    B[p] = A[per[p]]
B = list(map(list, zip(*B)))
C = B.copy()
per = np.random.permutation(c)
for p in range(len((per))):
    B[p] = C[per[p]]
B = list(map(list, zip(*B)))



P = []
Q = []
#finding P
arr = []
for i in range(r):
    for j in range(r):
        if isPermutation(np.asarray(B[i]).tolist(), np.asarray(A[j]).tolist()):
            arr+= [j]
            break

for i in range(r):
    d = []
    d += [0] * arr[i]
    d+=[1]
    d+= [0] *(r - arr[i] - 1)
    P += [d]

#finding Q
C = np.matmul(P, A)
a = []
for i in range(c):
    for j in range(c):
        if list(map(list, zip(*C)))[i] == list(map(list, zip(*B)))[j]:
            a += [j]
            break

for i in range(c):
    d = [0] * a[i] + [1] + [0] *(r - a[i])
    Q.append(d)




print("P:")
print(np.matrix(P))
print("Q:")
print(np.matrix(Q))
print("PAQ = ")
print(np.matmul(np.matmul(P, A), np.matrix(Q)))
print("Which equals B")
print(np.matrix(B))
