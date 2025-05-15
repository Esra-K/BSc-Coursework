import sys
import numpy as np
from collections import defaultdict
from itertools import combinations
from sklearn import svm
from sklearn.metrics import ndcg_score
import json


def rec_dd():
    return defaultdict(rec_dd)


def sign(x):
    return 1 if x > 0 else 0 if x == 0 else -1


def read_data(s, j):
    data = []
    for i in range(1, j + 1):
        with open('MQ2008/Fold' + str(i) + '/' + str(s) + '.txt') as f:
            data += [x.rstrip('\n') for x in f]
    return data


def structure_data(data_array):
    x_d = rec_dd()
    y_d = rec_dd()
    for e in data_array:
        element = e.split(" ")
        y = int(element[0])
        qid = int(element[1][4:])
        vect = np.zeros(46)
        for i in range(2, 48):
            xi = element[i]
            vect[i - 2] = float(xi[xi.find(':') + 1:])
        docid = element[50]
        x_d[qid][docid] = vect
        y_d[qid][docid] = y
    return x_d, y_d


def pairwise_transition2(x_dict, y_dict):
    n_samples = sum([len(
        [(i, j) for i, j in list(combinations(list(x_dict[query].keys()), 2)) if y_dict[query][i] != y_dict[query][j]])
                     for query in x_dict.keys()])
    X = np.zeros((n_samples, 46))
    y = np.zeros(n_samples)
    k = 0
    for query in x_dict.keys():
        xvals = x_dict[query]
        yvals = y_dict[query]
        for i, j in list(combinations(list(xvals.keys()), 2)):
            if yvals[i] != yvals[j]:
                X[k] = xvals[i] - xvals[j]
                y[k] = sign(yvals[i] - yvals[j])
                k += 1
    # print(k == n_samples)
    return X, y


n = 5

train = read_data("train", n)
x_dic, y_dic = structure_data(train)
X_train, y_train = pairwise_transition2(x_dic, y_dic)

vali = read_data("vali", n)
x_dic, y_dic = structure_data(vali)
X_vali, y_vali = pairwise_transition2(x_dic, y_dic)

# print(X_train.shape, y_train.shape)
# print(X_vali.shape, y_vali.shape)
# print(X_test.shape, y_test.shape)

# print(X_train[:100])
# print(y_train[:100])
# print(list(y_train).count(1))
# print(list(y_vali).count(1))
# print(list(y_test).count(1))

# print(list(y_train).count(-1))
# print(list(y_vali).count(-1))
# print(list(y_test).count(-1))

cs = [0.01, 0.1, 1, 10, 100]
scores = [0. for i in range(5)]
for i in range(len(cs)):
    svm1 = svm.SVC(kernel="linear", C=cs[i])
    clf = svm1.fit(X_train, y_train)
    scores[i] = svm1.score(X_vali, y_vali)

print("Scores for different c params: Params:", cs, "Respective scores:", scores)
max_value = max(scores)
max_index = scores.index(max_value)
c = cs[max_index]

# c = 10

svm1 = svm.SVC(kernel="linear", C=c)
clf = svm1.fit(X_train, y_train)

test = read_data("test", n)
x_dic, y_dic = structure_data(test)
# X_test, y_test = pairwise_transition(x_dic, y_dic)
w = svm1.coef_[0]

ndcg_scores = defaultdict(float)
for query in x_dic.keys():
    query_vecs = x_dic[query]
    query_y = y_dic[query]
    real_scores = []
    predicted_scores = []
    for doc in query_y.keys():
        predicted_scores.append(np.dot(query_vecs[doc], w))
        real_scores.append(query_y[doc])
    if max(real_scores) != min(real_scores):
        ndcg_scores[query] = ndcg_score(np.asarray([real_scores]), np.asarray([predicted_scores]), k=min(5, len(real_scores)))

with open("full_ndcg.txt", "w") as ndcg:
    json.dump(ndcg_scores, ndcg, indent=4)

print("Mean NDCG:", np.mean(list(ndcg_scores.values())))
