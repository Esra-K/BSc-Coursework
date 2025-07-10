from sklearn.datasets import load_iris
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

iris = load_iris()
xxxx = iris.data
yyyy = iris.target
xxxx = np.c_[xxxx, yyyy]
np.random.shuffle(xxxx)
partition = int(0.8 * len(xxxx))
x_trn, x_tst = xxxx[:partition, :], xxxx[partition:, :]
y_trn = x_trn[:, -1]
y_tst = x_tst[:, -1]
x_trn = np.delete(x_trn, np.s_[len(x_trn[0]) - 1:], axis=1)
x_tst = np.delete(x_tst, np.s_[len(x_tst[0]) - 1:], axis=1)


# 1 ezafe mikone sotoone avval
def calcPhimat(X):
    N = len(X)
    if len(np.shape(X)) == 1:
        d = 1
    else:
        d = np.shape(X)[1]
    Phi = np.zeros((N, d + 1))
    Phi[:, 0] = np.ones(N)
    Phi[:, 1:] = np.reshape(X, (N, d))
    return Phi


# classe dadeha ro one-hot mikone
def calcTmat(y, C):
    N = len(y)
    T = np.zeros((N, C))
    for c in range(C):
        T[:, c] = (y == c)
    return T


# 1)zarb 2)normalize by softmax
def calcPmat(Theta, Phi):
    P = np.exp(Phi @ (Theta.T))
    P = P / np.reshape(np.sum(P, axis=1), (len(Phi), 1))
    return P


def cost_function(thtvec, Phi, T, lam):
    N, M = np.shape(Phi)
    C = np.shape(T)[1]
    Theta = np.reshape(thtvec, (C, M))
    P = calcPmat(Theta, Phi)
    J = -1.0 / N * np.sum(T * np.log(P)) + lam / (2.0 * N) * np.linalg.norm(thtvec) ** 2
    return J


def grad_cost_function(thtvec, Phi, T, lam):
    N, M = np.shape(Phi)
    C = np.shape(T)[1]
    Theta = np.reshape(thtvec, (C, M))
    P = calcPmat(Theta, Phi)
    grad_mat = 1.0 / N * ((P - T).T) @ Phi + lam / N * Theta
    grad_vec = np.reshape(grad_mat, len(thtvec))
    return grad_vec


def minimize_GD(X, y, func, x0, grad, alpha=0.01, maxiter=1e4, ftol=1e-5):
    err_arr = []
    x = x0
    nit = 0
    while nit < maxiter:
        theta = np.reshape(x, (3, 5))
        t = calcPmat(theta, calcPhimat(X))
        ypred = np.argmax(t, axis=1)
        err_arr.append(len([i for i in range(len(ypred)) if ypred[i] != y[i]]))
        xold = x
        x = x - alpha * grad(x)
        nit += 1
        if abs(func(x) - func(xold)) < ftol:
            break
    plt.plot(err_arr)
    plt.xlabel("Num of Iterations")
    plt.ylabel("Num of Misclassifications")
    plt.show()
    success = (nit < maxiter)
    return {'x': x, 'nit': nit, 'func': func(x), 'success': success}


class LogisticClf:
    def __init__(self, C, lam):
        self.C = C  
        self.lam = lam  
        self.Theta = None

    def fit(self, X, y, alpha=None, maxiter=10000, ftol=1e-5):
        Phi = calcPhimat(X)
        T = calcTmat(y, self.C)
        N, M = np.shape(Phi)
        tht0 = np.zeros(M * self.C)
        result = minimize_GD(X, y, func=lambda x: cost_function(x, Phi, T, self.lam),
                             x0=tht0,
                             grad=lambda x: grad_cost_function(x, Phi, T, self.lam),
                             alpha=alpha,
                             maxiter=maxiter,
                             ftol=ftol)
        self.Theta = np.reshape(result['x'], (self.C, M))

    def predict(self, X):
        tmp = calcPmat(self.Theta, calcPhimat(X))
        return np.argmax(tmp, axis=1)


clf = LogisticClf(C=3, lam=10)
clf.fit(x_trn, y_trn, alpha=0.01)
y_pred = clf.predict(x_tst)
print("Accuracy:", len([i for i in range(len(y_pred)) if y_pred[i] == y_tst[i]]) * 100 / len(y_pred))

cm = np.zeros((clf.C, clf.C))
for i in range(len(y_pred)):
    pred = int(y_pred[i])
    real = int(y_tst[i])
    cm[pred][real] += 1
print("Confusion matrix (row indices are predicted values, column indices are real values)")
print(pd.DataFrame(cm))
