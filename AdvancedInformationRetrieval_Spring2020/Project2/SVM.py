import json
import codecs
from collections import defaultdict
from math import log, sqrt, pi, e
import numpy as np
from collections import Counter
from sklearn import svm


def process(raw_text):
    punctuations = "!@#$%^&?<>*()[}{]-=/|~`+_'.,:;؛،\؟«»ٰ'\"\\\t\n"
    text = raw_text
    for p in punctuations:
        text = text.replace(p, " ")
    return [x for x in text.split(" ") if not x == '']


def read_json(filepath):
    return json.load(codecs.open(filepath, 'r', 'utf-8-sig'))


def get_term_set(filename, subset_index):
    test_set = read_json(filename)
    test_set = test_set[:len(test_set) // subset_index]
    term_set = set()
    for i, element in enumerate(test_set):
        title_words = process(element['title'])
        body_words = process(element['body'])

        for word in title_words + body_words:
            term_set.add(word)
    return term_set


def get_dataset(term_set, filename, weight, subset_index):
    test_set = read_json(filename)
    test_set = test_set[:len(test_set) // subset_index]
    real_classes = [0. for i in range(len(test_set))]

    X = np.array([[0. for j in range(len(term_set))] for i in range(len(test_set))], dtype=np.float16)
    D = len(test_set)
    idf = defaultdict(int)
    for i, element in enumerate(test_set):
        title_words = process(element['title'])
        body_words = process(element['body'])
        real_classes[i] = element['category']

        title_dict = dict(Counter(title_words))
        for key in title_dict.keys():
            title_dict[key] *= weight
        body_dict = dict(Counter(body_words))

        aggregate_dict = {k: title_dict.get(k, 0) + body_dict.get(k, 0)
                          for k in set(title_dict) | set(body_dict)}

        for ind, term in enumerate(term_set):
            if term in aggregate_dict.keys():
                X[i][ind] = aggregate_dict[term]
                idf[term] += 1

    idf_dict = {term: log((1 + D) / (1 + idf[term])) for term in idf.keys()}

    for i in range(len(test_set)):
        for ind, term in enumerate(term_set):
            X[i][ind] *= idf_dict[term]
    return X, real_classes


set1 = get_term_set('train.txt', subset_index=3)
set2 = get_term_set('test.txt', subset_index=2)
joint_set = set1 & set2

X_train, y_train = get_dataset(joint_set, 'train.txt', weight=5, subset_index=3)
X_test, y_test = get_dataset(joint_set, 'test.txt', weight=5, subset_index=2)

clf = svm.SVC(kernel='linear')

print("I got here")
clf.fit(X_train, y_train)
print("I got here 2")
y_pred = clf.predict(X_test)

acc = 0
for i in range(len(y_test)):
  if y_test[i] == y_pred[i]:
    acc += 1

print(acc/ len(y_test))