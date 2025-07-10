import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import math
pd.set_option('display.max_columns', 500)


def mse(pred, real):
    err = 0.
    n = len(pred)
    for i in range(n):
        err += (pred[i] - real[i]) ** 2
    return err / n


def split_xy(dtst):
    x1 = dtst.drop(['Price'], axis=1).values
    y1 = dtst['Price'].values
    return x1, y1


xls = pd.ExcelFile('ToyotaCorolla.xls')
df = pd.read_excel(xls, 'data', header=0)
df = df.drop('Id', axis=1)
df = df.drop('Model', axis=1)

df2 = pd.get_dummies(df['Fuel_Type']).drop('Petrol', axis=1)
df3 = pd.get_dummies(df['Color']).drop('Yellow', axis=1)
df = pd.concat([df, df2], axis=1)
df = pd.concat([df, df3], axis=1)
df = df.drop('Fuel_Type', axis=1)
df = df.drop('Color', axis=1)
df = df.apply(lambda x: x/x.max(), axis=0)
df = df.dropna()

trn, val, tst = np.split(df.sample(frac=1, random_state=20), [int(.7 * len(df)), int(.85 * len(df))])
x_trn, y_trn = split_xy(trn)
x_val, y_val = split_xy(val)
x_tst, y_tst = split_xy(tst)


def plot(err_arr1, err_arr2):
    x_arr1 = [i for i in range(len(err_arr1))]
    plt.plot(x_arr1, err_arr1)
    x_arr2 = [i for i in range(len(err_arr2))]
    plt.plot(x_arr1, err_arr2)
    plt.legend(['validation', 'test'], loc='upper left')
    print("Validation MSE:", err_arr1[-1])
    print("Test MSE:", err_arr2[-1])
    plt.show()


class RidgeRegression:
    def __init__(self, learning_rate, iterations, l2_penalty):
        self.learning_rate = learning_rate      # for updating ws
        self.iterations = iterations      # number of iterations (epochs)
        self.l2_penalty = l2_penalty      # lambda parameter (coefficient of l1 norm in loss function)
        self.m = 0      # number of samples
        self.n = 0      # number of features
        self.W = np.array([])      # weight vector (ws)
        self.b = 0      # bias term (w0)
        self.X = np.array([])      # train data features
        self.Y = np.array([])      # train data ys

        self.xval = np.array([])      # validation data features
        self.yval = np.array([])      # validation data ys
        self.errval = []      # list of errors of validation data in each iteration

        self.xtst = np.array([])      # test data features
        self.ytst = np.array([])      # test data epochs
        self.errtst = []      # list of errors of test data in each iteration

    def fit(self, xtrn, ytrn, xval, yval, xtst, ytst):
        self.m, self.n = xtrn.shape
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = xtrn
        self.Y = ytrn
        self.xval = xval
        self.yval = yval
        self.xtst = xtst
        self.ytst = ytst
        # closed form formula for w
        self.W = np.matmul(np.matmul(np.linalg.inv(np.matmul(self.X.T, self.X) +
        self.l2_penalty * np.identity(self.n)), self.X.T), self.Y)
        # for i in range(self.iterations):
            # self.update_weights()
            # self.update_errs()
        # plot(self.errval, self.errtst)
        return self

    def update_errs(self):
        y1 = self.predict(self.xval)
        j = mse(y1, self.yval)
        self.errval.append(j)
        y2 = self.predict(self.xtst)
        j = mse(y2, self.ytst)
        self.errtst.append(j)
        return self

    # def update_weights(self):
    #     Y_pred = self.predict(self.X)
    #     dW = (- (2 * self.X.T.dot(self.Y - Y_pred)) +
    #           (2 * self.l2_penalty * self.W)) / self.m
    #     db = - 2 * (np.sum(self.Y - Y_pred) + self.l2_penalty * self.b) / self.m
    #
    #     self.W = self.W - self.learning_rate * dW
    #     self.b = self.b - self.learning_rate * db
    #     return self

    def predict(self, x):
        return x.dot(self.W) + self.b


def ridge_test(l2_penalt):
    model = RidgeRegression(iterations=100, learning_rate=0.03, l2_penalty=l2_penalt)
    model.fit(x_trn, y_trn, x_val, y_val, x_tst, y_tst)
    print("W when l2 penalty is", l2_penalt, ":")
    print(model.W)
    y_pred = []
    for i in x_tst:
        y_pred.append(model.predict(i))
    plt.scatter(x_tst[:, 0], y_tst, c='orange')
    plt.scatter(x_tst[:, 0], y_pred, c='red')
    plt.xlabel("x[:, 0] (1st feature)")
    plt.ylabel("y")
    plt.legend(['real test y', 'predicted test y'])
    plt.title("Ridge Regression, Lambda =" + str(l2_penalt))
    plt.show()
    return model.W


w1 = ridge_test(1)
w2 = ridge_test(0)

# subtract_absolutes = [(math.fabs(w1[i]) - math.fabs(w2[i])) / math.fabs(w1[i]) for i in range(len(w1))]
# print(sum([1 for a in subtract_absolutes if a < -0.01]) / len(subtract_absolutes))
# print(sum([1 for a in subtract_absolutes if a > 0.01]) / len(subtract_absolutes))

# Report:
# Less error with l2 regularization, although the weights did not change much.