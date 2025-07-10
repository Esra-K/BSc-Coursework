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
df = df.apply(lambda x: x / x.max(), axis=0)
df = df.dropna()

trn, val, tst = np.split(df.sample(frac=1, random_state=42), [int(.7 * len(df)), int(.85 * len(df))])
x_trn, y_trn = split_xy(trn)
x_val, y_val = split_xy(val)
x_tst, y_tst = split_xy(tst)


def plot(err_arr1, err_arr2):
    x_arr1 = [i for i in range(len(err_arr1))]
    plt.plot(x_arr1, err_arr1)
    x_arr2 = [i for i in range(len(err_arr2))]
    plt.plot(x_arr1, err_arr2)
    plt.legend(['validation', 'test'], loc='upper left')
    plt.title("MSE on each epoch")
    plt.xlabel("epoch")
    plt.ylabel("MSE")
    print("Validation MSE:", err_arr1[-1])
    print("Test MSE:", err_arr2[-1])
    plt.show()


def update_coef(learning_rate, error, w, data):
    ip = 1
    for i in range(len(data)):
        if ip == 1:
            w[0] = w[0] - learning_rate * error / (math.fabs(error))
            ip = ip + 1
        vx = learning_rate * error * data[i] / (math.fabs(error))
        w[i + 1] = w[i + 1] - vx
    return w


def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)):
        yhat += coefficients[i + 1] * row[i]
    return yhat


def coef_sgd_coefficient(train, y_train, xval, yval, xtst, ytst, epoch, learning_rate, r):
    weights = []
    val_err = []
    tst_err = []
    for i in range(0, len(train[0]) + 1):
        w_rand = np.random.uniform(0, r)
        weights.append(w_rand)

    for iteration in range(epoch):
        sum_of_error = 0
        y_predicted = 0
        idx = np.random.choice(np.arange(len(train)), 100, replace=False)
        x_sample = train[idx]
        y_sample = y_train[idx]
        for j, data in enumerate(x_sample):
            ip = 1
            for i in range(len(data)):
                if ip == 1:
                    y_predicted = weights[0]
                    ip = ip + 1
                y_predicted = y_predicted + weights[i + 1] * data[i]
            error = y_predicted - y_sample[j]
            sum_of_error = sum_of_error + error ** 2
            weights = update_coef(learning_rate, error, weights, data)

        y1 = list(map(predict, xval, itertools.repeat(weights, len(xval))))
        err1 = np.linalg.norm(yval - y1) ** 2
        val_err.append(err1)

        y2 = list(map(predict, xtst, itertools.repeat(weights, len(xtst))))
        err2 = np.linalg.norm(ytst - y2) ** 2
        tst_err.append(err2)
    plot(val_err, tst_err)
    return weights


w = coef_sgd_coefficient(x_trn, y_trn, x_val, y_val, x_tst, y_tst, epoch=100, learning_rate=0.008, r=1.5)

y_pred = []
for i in x_tst:
    y_pred.append(predict(i, w))
plt.scatter(x_tst[:, 0], y_tst, c='orange')
plt.scatter(x_tst[:, 0], y_pred, c='red')
plt.xlabel("x[:, 0] (1st feature)")
plt.ylabel("y")
plt.title("Predicted y vs Real y")
plt.legend(['real test y', 'predicted test y'])
plt.show()
