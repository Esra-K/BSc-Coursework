from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

iris = load_iris()
xxxx = iris.data
yyyy = iris.target
xxxx = np.c_[xxxx, yyyy]
xxxx = np.array([xxxx[i] for i in range(len(xxxx)) if xxxx[i][len(xxxx[i]) - 1] != 2])
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


x_trn = calcPhimat(x_trn)
x_tst = calcPhimat(x_tst)

w0 = np.zeros((1, len(x_trn[0])))
w1 = np.zeros((1, len(x_trn[0])))

misclass = 1000
lrning_rt = 0.5
epoch = 0
err_arr = []
while misclass > 0 and epoch < 100:
    misclass = 0
    for i, x in enumerate(x_trn):
        s1 = np.dot(np.reshape(x, (1, len(x))), w0.T)
        # s2 = np.dot(np.reshape(x, (1, len(x))), w1.T)
        verdict = 0 if s1 <= 0.5 else 1
        if verdict != y_trn[i]:
            misclass += 1
            if y_trn[i] == 0:
                w0 = w0 - lrning_rt * x
                # w1 = w1 - lrning_rt * x
            else:
                w0 = w0 + lrning_rt * x
                # w1 = w1 + lrning_rt * x
    err_arr.append(misclass)
    # print(misclass)
    # print(w0)
    # print(w1)
    epoch += 1

plt.plot(err_arr)
plt.xlabel("Num of Iterations")
plt.ylabel("Num of Misclassifications")
plt.show()

y_pred = np.array([0] * len(y_tst))
for i, x in enumerate(x_tst):
    s1 = np.dot(np.reshape(x, (1, len(x))), w0.T)
    # s2 = np.dot(np.reshape(x, (1, len(x))), w1.T)
    y_pred[i] = 0 if s1 <= 0.5 else 1

print("Accuracy:", len([i for i in range(len(y_pred)) if y_pred[i] == y_tst[i]]) * 100 / len(y_pred))

cm = np.zeros((2, 2))
for i in range(len(y_pred)):
    pred = int(y_pred[i])
    real = int(y_tst[i])
    cm[pred][real] += 1

print("Num of epochs:", epoch)
print("Confusion matrix (row indices are predicted values, column indices are real values)")
print(pd.DataFrame(cm))
