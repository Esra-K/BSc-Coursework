from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import e
pd.set_option('display.max_columns', 500)


# (X_TX)−1X_Ty would not work when X_TX was singular
def closed_form_reg(x, y):
    xTemp = np.c_[np.ones(x.shape[0]), x]
    # xt = np.transpose(xTemp)
    # xxtinv = np.linalg.inv(np.matmul(xt, xTemp))
    # betaHat = np.matmul(np.matmul(xxtinv, xt), y)
    beta_hat = np.linalg.lstsq(xTemp, y, rcond=None)[0]
    return beta_hat


def find_y_pred(x, betahat):
    xTemp = np.c_[np.ones(x.shape[0]), x]
    yHat = betahat.dot(xTemp.T)
    return yHat


def mse(pred, real):
    if len(pred) != len(real):
        print("wrong lengths")
    err = 0.
    n = len(pred)
    for i in range(n):
        err += (pred[i] - real[i]) ** 2
    return err / n


def add_second_order(dtfrm):
    d = dtfrm
    for i in range(13):
        d[i + 15] = d[i] ** 2
    return d


# X, y = load_boston(return_X_y=True)

# load dataset
boston = load_boston()
X = boston['data']
y = boston['target']
names = boston['feature_names']


def plot_predicted_vs_real_by_13_columns(question_indicator, pred_index, real_index, dtfrm):
    global names
    for i in range(13):
        ax = dtfrm.plot(kind="scatter", x=i, y=pred_index, color="b", label="Question " + str(question_indicator)
                                                                            + ": column " + names[i] + " vs. predicted y")
        dtfrm.plot(kind="scatter", x=i, y=real_index, color="r", label="Question " + str(question_indicator)
                                                                       + ": column " + names[i] + " vs. real y", ax=ax)
        ax.set_xlabel(str(i))
        ax.set_ylabel("y predicted & real")
        plt.show()


# print(X.shape)
# print(y.shape)
# X = np.array(X)
# y = np.array(y)
# print(type(X))
# print(type(y))
# print(y)

nans = []

# check for nans
for i in range(len(X)):
    for j in range(len(X[i])):
        if not isinstance(X[i][j], float) or np.isnan(X[i][j]) or np.isinf(X[i][j]) or X[i][j] != X[i][j]:
            nans.append(i)

for i in range(len(y)):
    if not isinstance(y[i], float) or np.isnan(y[i]) or np.isinf(y[i]) or y[i] != y[i]:
        nans.append(i)

# remove rows with nans
X = np.array([X[i] for i in range(len(X)) if not i in nans])
y = np.array([y[i] for i in range(len(y)) if not i in nans])

# split into train & test
X2 = np.c_[X, y]
df = pd.DataFrame(X2)
# print(df)
train = df.sample(frac=0.8, random_state=200)  # random state is a seed value
test = df.drop(train.index)
# print(train.head())
# print(test.head())
# print(list(map(type, list(df.columns.values))))

# plot target value by other columns
yOfDf = train[13]

for i in range(13):
    # df.plot(x=i, y=13, style='o')
    # plt.show()
    # m, b = np.polyfit(df[i], yOfDf, 1)
    b, m = closed_form_reg(train[i], yOfDf)
    # print(b, m)

    yp = np.polyval([m, b], train[i])
    plt.plot(train[i], yp)
    plt.grid(True)
    plt.scatter(train[i], yOfDf)
    plt.title("Question 2: target value by " + names[i])
    plt.xlabel(names[i])
    plt.ylabel("y")
    plt.show()


# correlation matrix & heatmap

plt.matshow(train.corr())
plt.xticks(range(train.shape[1]), train.columns, fontsize=14, rotation=45)
plt.yticks(range(train.shape[1]), train.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
a = [n3 for n3 in names] + ["y"]
plt.xticks(range(train.shape[1]), a, fontsize=14, rotation=45)
plt.yticks(range(train.shape[1]), a, fontsize=14)
# plt.title('Correlation Matrix', fontsize=16)
plt.show()


# Question 3: 1st regression
beta = closed_form_reg(train.loc[:, 0:12], train[13])
# print(beta)
train[14] = find_y_pred(train.loc[:, 0:12], beta)
# print(list(train[14]))

# print(train.head())
test[14] = find_y_pred(test.loc[:, 0:12], beta)
# print(test.loc[:, 13:14])
# print(test.head())

# plot test results for each column of the original DF
plot_predicted_vs_real_by_13_columns(3, 14, 13, test)

# Question 6 for part 3
print("Question 3: train set mse:", mse(list(train[14]), list(train[13])))
print("Question 3: test set mse:", mse(list(test[14]), list(test[13])))


# Question 4: add 2nd order columns
train = add_second_order(train)
test = add_second_order(test)
# print(test[2], "\n", test[17])
# print(list(train.columns.values))
# print(list(test.columns.values))


def df_for_reg_with_2nd_order(dtfrm):
    return dtfrm
    # return dtfrm.loc[:, list(range(14)) + list(range(15, 28))]


def rearrange(dtfrm, dest, src):
    cols = list(dtfrm)
    # move the column to head of list using index, pop and insert
    cols.insert(dest, cols.pop(cols.index(src)))
    d = dtfrm.loc[:, cols]
    return d


# change columns' order to pass the DF to the regression function more easily
train2 = rearrange(train, 0, 13)
train2 = rearrange(train2, 0, 14)

test2 = rearrange(test, 0, 13)
test2 = rearrange(test2, 0, 14)

# print(list(train2.columns.values))
# print(list(test2.columns.values))

# Question 4: regression with 2nd order columns
beta2 = closed_form_reg(train2.loc[:, list(set(range(28)) - set(list([13, 14])))], train2[13])
train2[28] = find_y_pred(train2.loc[:, list(set(range(28)) - set(list([13, 14])))], beta2)
test2[28] = find_y_pred(test2.loc[:, list(set(range(28)) - set(list([13, 14])))], beta2)

# plot test results for each column of the original DF
plot_predicted_vs_real_by_13_columns(4, 28, 13, test2)


# Question 6 for part 4
print("Question 4: train set mse:", mse(list(train2[28]), list(train2[13])))
print("Question 4: test set mse:", mse(list(test2[28]), list(test2[13])))


# Question 5: start from here
train3 = rearrange(train2, 0, 28)
test3 = rearrange(test2, 0, 28)

train3 = train3.loc[:, list(set(range(28)) - set(range(15, 28)))]
test3 = test3.loc[:, list(set(range(28)) - set(range(15, 28)))]

# 10 random samples as mu vectors
meows = train3.sample(n=10)

# rearrange columns again
train3 = rearrange(train3, 0, 13)
train3 = rearrange(train3, 0, 14)
test3 = rearrange(test3, 0, 13)
test3 = rearrange(test3, 0, 14)
meows = rearrange(meows, 0, 13)
meows = rearrange(meows, 0, 14)

# print(list(train3.columns.values))
# print(list(test3.columns.values))
# print(list(meows.columns.values))


# gaussian formula
def gaussian(r, mw, sigma=1):
    r2 = np.array(r)
    # print(r2)
    r2 = r2[2:15]
    mw2 = mw[2:15]
    nrm = np.linalg.norm(r2 - mw2) ** 2
    return e ** ((-1) * nrm / (2 * sigma ** 2))


# print(test3.apply(lambda row: type(row), axis=1))

# adds the 10 metrics to the sets rows
def add_meow_metric(meow_list, dtfrm):
    d = dtfrm
    k = 0
    for index, row in meow_list.iterrows():
        # print(row)
        mew = np.array(row)
        # print(m)
        d[15 + k] = d.apply(lambda rw: gaussian(rw, mew), axis=1)
        k += 1
    return d


train3 = add_meow_metric(meows, train3)
test3 = add_meow_metric(meows, test3)
# print(train3)
# print(test3)

# Question 5: regression
beta3 = closed_form_reg(train3.loc[:, list(set(range(15, 25)).union(set(range(13))))], train3[13])
train3[25] = find_y_pred(train3.loc[:, list(set(range(15, 25)).union(set(range(13))))], beta3)
test3[25] = find_y_pred(test3.loc[:, list(set(range(15, 25)).union(set(range(13))))], beta3)

# plot test results for each column of the original DF
plot_predicted_vs_real_by_13_columns(5, 25, 13, test3)

# Question 6 for part 5
print("Question 5: train set mse:", mse(list(train3[25]), list(train3[13])))
print("Question 5: test set mse:", mse(list(test3[25]), list(test3[13])))

print("\nAnalysis (question 6): using higher order values of features helped \n"
      "and decreased the test data loss by about 24 percent, whereas using gaussian basis functions \n"
      "increased the loss of the test set by a factor of 3.5, and plots indicate that the corresponding model\n"
      "is severely underfit, predicting almost the same target value for all test data. However, using \n"
      "these basis functions along with the original 13 features improves the results by a small degree\n"
      "on the train set, but deteriorates them on the test set. One major upgrade would be employing the \n "
      "K-means method to find 10 good mu values rather than random points from the training set. Hence the best \n"
      "method was the one involving 2nd order values of features.\n")


def part6_plt(pred, real, dtfrm, title):
    plt.scatter(dtfrm[pred], dtfrm[real], c="b")

    plt.xlabel("pred")
    plt.ylabel("real")
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


part6_plt(14, 13, test, "Question3")
part6_plt(28, 13, test2, "Question4")
part6_plt(25, 13, test3, "Question5")

