import numpy as np

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

def SVM(a):
    tolerance = 10**-16/(len(a)**2)
    u = np.eye(len(a))
    s = np.transpose(a)

    v = np.eye(len(a))
    # print("U:", u)
    # print("S:", s)
    # print("V", v)
    Err = 10000
    iter = 0
    while Err > tolerance:
        q, s = qr(np.transpose(s))
        # print("part", iter+1, ":")
        # print("q:", q)
        # print("s:", s)
        u = np.matmul(u, q)
        # print("U:", u)
        q, s = qr(np.transpose(s))
        # print("q:", q)
        # print("S:", s)
        v = np.matmul(v, q)
        # print("V", v)
        e = np.triu(s, 1) #shayad 1 bood
        #print("e:", e)
        E = np.linalg.norm(e)
        #print("E", E)
        F = np.linalg.norm(np.diag(s))
        #print("F", F)
        if F == 0:
            F=1
        Err = E / F

    # ss = np.diag(s)
    # s = []
    # for i in range(len(a)):
    #     sk = []
    #     for j in range(len(a)):
    #         sk.append(0.)
    #     s.append(sk)
    # for n in range(len(ss)):
    #     s[n][n] = abs(ss[n])
    #     if ss[n] < 0:
    #         for i in range(len(a)):
    #             u[i][n] = -1 * u[i][n]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if i == j:
                if s[i][j] < 0:
                    s[i][j] = -s[i][j]
                    for k in range(len(s)):
                        u[k][i] = -u[k][i]
            else:
                s[i][j] = 0
    return u, s, np.transpose(v)

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
a = np.array(A)

U, S, V = SVM(a)
b = 8
U = U.round(b)
S = np.array(S).round(b)
V = V.round(b)
V = np.transpose(V)

for i in range(len(U)):
    for j in range(len(U[i])):
        if j == len(U[i]) - 1:
            print(U[i][j], end="\n")
        else:
            print(U[i][j], end=" ")

for i in range(len(S)):
    for j in range(len(S[i])):
        if j == len(S[i]) - 1:
            print(S[i][j], end="\n")
        else:
            print(S[i][j], end=" ")

for i in range(len(V)):
    for j in range(len(V[i])):
        if j == len(V[i]) - 1:
            print(V[i][j], end="\n")
        else:
            print(V[i][j], end=" ")
# print(np.matmul(U, np.matmul(S, np.transpose(V))))
# print(np.matmul(U, np.transpose(U)))
# print(np.matmul(V, np.transpose(V)))