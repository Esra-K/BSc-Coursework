import cvxopt
from cvxopt import matrix as cvxopt_matrix
from cvxopt import solvers as cvxopt_solvers
from sklearn.datasets import load_digits
import numpy as np
import random

# this code uses gaussian kernel.
# To use linear kernel, replace the term gkernel in line 177 and line 213 with linkernel

# linear kernel: optimal C: 1. accuracy score: 0.95
# gaussian kernel: optimal C: 1. accuracy score: 0.9944444444444445

class LinearKernel:
    def __init__(self, theta=None):
        pass

    def __call__(self, X, Y):
        return X @ Y.T


class GaussianKernel:
    def __init__(self, theta):
        self.theta = theta

    def __call__(self, X, Y):
        if (X.ndim == 1) and (Y.ndim == 1):
            tmp = np.linalg.norm(X - Y) ** 2
        elif ((X.ndim == 1) and (Y.ndim != 1)) or ((X.ndim != 1) and (Y.ndim == 1)):
            tmp = np.linalg.norm(X - Y, axis=1) ** 2
        else:
            tmp = np.reshape(np.sum(X ** 2, axis=1), (len(X), 1)) + np.sum(Y ** 2, axis=1) - 2 * (X @ Y.T)
        K = np.exp(- tmp / (2 * self.theta ** 2))
        return K


class SVC:
    def __init__(self, kernel, C=1.0):
        self.C = C
        self.kernel = kernel

    def fit(self, X, y):
        m, n = X.shape
        y = y.reshape(-1, 1) * 1.
        X_dash = y * X
        H = self.kernel(X_dash, X_dash) * 1.

        P = cvxopt_matrix(H)
        q = cvxopt_matrix(-np.ones((m, 1)))
        G = cvxopt_matrix(np.vstack((np.eye(m) * -1, np.eye(m))))
        h = cvxopt_matrix(np.hstack((np.zeros(m), np.ones(m) * self.C)))
        A = cvxopt_matrix(y.reshape(1, -1))
        b = cvxopt_matrix(np.zeros(1))

        sol = cvxopt_solvers.qp(P, q, G, h, A, b)
        self.alphas = np.array(sol['x'])

        self.w = ((y * self.alphas).T @ X).reshape(-1, 1)
        self.S = (self.alphas > 1e-4).flatten()
        self.b = y[self.S] - self.kernel(X[self.S], self.w.T)

        # print(len(self.alphas), len(self.alphas[self.alphas > 10 ** -4]))
        # print('Alphas = ', self.alphas[self.alphas > 1e-4])
        # print('w = ', self.w.flatten())
        # print('b = ', self.b[0])

        inds = [i for i in range(len(self.alphas)) if self.alphas[i] > 10**-4]
        self.X_sv = X[inds]
        self.t_sv = y[inds]
        self.a = self.alphas[inds]
        self.b1 = np.mean(self.b)

    def decision_function(self, X):
        val_dec_func = self.kernel(X, self.X_sv) @ (self.a * self.t_sv) + self.b1
        return val_dec_func



# Load data
digits = load_digits()
x = digits.data
y = digits.target

# Normalize
for i in range(len(x)):
    x[i] = x[i] / np.linalg.norm(x[i])

# split train and test in a way which ensures that
# at least 15 data of each label are present in the test set
# source: https://stackoverflow.com/questions/35472712/how-to-split-data-on-balanced-training-set-and-test-set-on-sklearn
def split_balanced(data, target, test_size):
    classes = np.unique(target)

    if test_size < 1:
        n_test = np.round(len(target) * test_size)
    else:
        n_test = test_size
    n_train = max(0, len(target) - n_test)
    n_train_per_class = max(1, int(np.floor(n_train / len(classes))))
    n_test_per_class = max(1, int(np.floor(n_test / len(classes))))

    ixs = []
    for cl in classes:
        if (n_train_per_class + n_test_per_class) > np.sum(target == cl):

            splitix = int(np.ceil(n_train_per_class / (n_train_per_class + n_test_per_class) * np.sum(target == cl)))
            ixs.append(np.r_[np.random.choice(np.nonzero(target == cl)[0][:splitix], n_train_per_class),
                             np.random.choice(np.nonzero(target == cl)[0][splitix:], n_test_per_class)])
        else:
            ixs.append(np.random.choice(np.nonzero(target == cl)[0], n_train_per_class + n_test_per_class,
                                        replace=False))

    ix_train = np.concatenate([x[:n_train_per_class] for x in ixs])
    ix_test = np.concatenate([x[n_train_per_class:(n_train_per_class + n_test_per_class)] for x in ixs])

    X_train = data[ix_train, :]
    X_test = data[ix_test, :]
    y_train = target[ix_train]
    y_test = target[ix_test]

    return X_train, X_test, y_train, y_test

x_trn, x_tst, y_trn, y_tst = split_balanced(x, y, 0.1)

# backup
x_t2 = x_trn
y_t2 = y_trn


# cross validation:

#initialize kernels
linkernel = LinearKernel()
gkernel = GaussianKernel(theta=0.2)
svm_list = []

# I used only half the data for cross validation to save time
x_t = x_trn
y_t = y_trn
c = list(zip(x_t, y_t))
random.shuffle(c)
x_t, y_t = zip(*c)
x_t = np.asarray(x_t)
y_t = np.asarray(y_t)
l = len(x_t)//2
x_t = x_t[:l, :]
y_t = y_t[:l]

# Hyperparameter candidates
cs = [1., 10, 100]
# accuracy scores for each hyperparameter
results = [0] * 3
# num of folds
k = 4
idx = [i * len(x_t) // k for i in range(k + 1)]

for u, c in enumerate(cs):
    mean_acc = 0
    for j in range(k):
        # train-validation split
        partition = range(idx[j], idx[j+1])
        x_valid = np.array([x_t[p] for p in range(len(x_t)) if p in partition])
        x_trn = np.array([x_t[p] for p in range(len(x_t)) if not p in partition])

        y_valid = np.array([y_t[p] for p in range(len(y_t)) if p in partition])
        y_trn = np.array([y_t[p] for p in range(len(y_t)) if not p in partition])

        # one-hot vectors for data labels
        y1 = np.zeros((len(y_trn), 10))
        for i in range(len(y_trn)):
            for j in range(10):
                if y_trn[i] == j:
                    y1[i][j] = 1
                else:
                    y1[i][j] = -1
        # y2 is used for prediction
        y2 = np.zeros((len(x_valid), 10))
        # One-vs-all: 10 SVM instances, one for each label
        for i in range(10):
            s = SVC(kernel=gkernel, C=10)
            s.fit(x_trn, y1[:, i])
            svm_list.append(s)
            y2[:, i] = s.decision_function(x_valid).reshape((len(y2[:, i], )))
        # classify validation set based on scores
        y3 = np.argmax(y2, axis=1)
        # accuracy score
        acc = len([i for i in range(len(y_valid)) if y_valid[i] == y3[i]])/ len(y3)
        mean_acc += acc
    results[u] = mean_acc

# choose c based on results
c = cs[np.argmax(results)]
print(c)

# retrieve original data
x_trn = x_t2
y_trn = y_t2

# one-hot vectors for data labels
y1 = np.zeros((len(y_trn), 10))
for i in range(len(y_trn)):
    for j in range(10):
        if y_trn[i] == j:
            y1[i][j] = 1
        else:
            y1[i][j] = -1

# print(list(zip(y_trn, y1)))

svm_list = []

# y2 is used for prediction
y2 = np.zeros((len(x_tst), 10))
# One-vs-all: 10 SVM instances, one for each label
for i in range(10):
    s = SVC(kernel=gkernel, C=c)
    s.fit(x_trn, y1[:, i])
    svm_list.append(s)
    y2[:, i] = s.decision_function(x_tst).reshape((len(y2[:, i], )))
# classify validation set based on scores
y3 = np.argmax(y2, axis=1)
acc = len([i for i in range(len(y_tst)) if y_tst[i] == y3[i]])/ len(y3)
# accuracy score
print(acc)
