import json
import codecs
from collections import defaultdict
from math import log, sqrt, pi, e
from collections import Counter
import operator
import numpy as np
from nltk import word_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

stemmer = SnowballStemmer('english')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']',
                   '{', '}', '!', '@', '#', '$', '%', '^', '&', '?', '<', '>'
                   '*', '-', '+', '/', '\\', '_', ''])

fanciness_decoder = [False, False, True]


def fancy_process(raw_text):
    global fanciness_decoder
    global lemmatizer, stemmer
    pretty_words = [i for i in word_tokenize(raw_text.lower())]
    if fanciness_decoder[0]:
        pretty_words = [i for i in pretty_words if i not in stop_words]
    if fanciness_decoder[1]:
        pretty_words = list(map(lemmatizer.lemmatize, pretty_words))
    if fanciness_decoder[2]:
        pretty_words = list(map(stemmer.stem, pretty_words))
    return pretty_words


def read_json(filepath):
    return json.load(codecs.open(filepath, 'r', 'utf-8-sig'))


def dict_level_one_list():
    return defaultdict(list)


def dict_level_one_int():
    return defaultdict(float)


def process(raw_text):
    punctuations = "!@#$%^&?<>*()[}{]-=/|~`+_'.,:;؛،\؟«»ٰ'\"\\\t\n"
    text = raw_text
    for p in punctuations:
        text = text.replace(p, " ")
    return [x for x in text.split(" ") if not x == '']


word_dict = defaultdict(dict_level_one_int)
class_counts = defaultdict(int)

train_set = read_json('train.txt')
test_set = read_json('test.txt')
fancy = 1
weight = 5
idf = defaultdict(float)
for i, element in enumerate(train_set):
    if fancy == 1:
        title_words = fancy_process(element['title'])
        body_words = fancy_process(element['body'])
    else:
        title_words = process(element['title'])
        body_words = process(element['body'])
    data_class = element['category']

    title_dict = dict(Counter(title_words))
    for key in title_dict.keys():
        title_dict[key] *= weight
    body_dict = dict(Counter(body_words))

    aggregate_dict = {k: title_dict.get(k, 0) + body_dict.get(k, 0)
                      for k in set(title_dict) | set(body_dict)}

    for key in aggregate_dict.keys():
        word_dict[key][data_class] += aggregate_dict[key]
        idf[key] += 1

    class_counts[data_class] += 1

D = len(train_set)
idf_dict = {term : log((1 + D) / (1 + idf[term])) for term in word_dict.keys()}

test_dict = defaultdict(dict_level_one_int)
test_real_classes = [0. for i in range(len(test_set))]
for i, element in enumerate(test_set):
    if fancy == 1:
        title_words = fancy_process(element['title'])
        body_words = fancy_process(element['body'])
    else:
        title_words = process(element['title'])
        body_words = process(element['body'])
    data_class = element['category']

    test_real_classes[i] = data_class

    title_dict = dict(Counter(title_words))
    for key in title_dict.keys():
        title_dict[key] *= weight
    body_dict = dict(Counter(body_words))

    aggregate_dict = {k: title_dict.get(k, 0) + body_dict.get(k, 0)
                      for k in set(title_dict) | set(body_dict)}

    for key in aggregate_dict.keys():
        if key in word_dict.keys():
            test_dict[i][key] = aggregate_dict[key]

for term, classes in word_dict.items():
    for c in classes.keys():
        word_dict[term][c] *= idf_dict[term]

for i, term_dict in test_dict.items():
    for term, tf in term_dict.items():
        test_dict[i][term] *= idf_dict[term]

sorted_classes = sorted(class_counts.keys())
acc = 0
predictions = [0. for i in range(len(test_set))]
alpha = 10.4
V = len(word_dict)
all_freq = {c:sum(word_dict[term][c] for term in word_dict.keys()) for c in sorted_classes}
for i, term_dict in test_dict.items():
    score = {key: log((class_counts[key] / len(train_set))) for key in sorted_classes}
    for term in term_dict.keys():
        for c in sorted_classes:
            score_i = log((word_dict[term][c] + alpha) / (all_freq[c] + alpha * V))
            score[c] += score_i
    predicted = max(score.items(), key=operator.itemgetter(1))[0]
    predictions[i] = predicted
    if predictions[i] == test_real_classes[i]:
        # print("hurray")
        acc += 1

# print(acc / len(test_set))


def dont_be_zero(num):
    return max(2 ** -16, num)


def evaluation(predicted, real):
    d = dict(Counter(zip(predicted, real)))

    confusion_mat = np.array([[0. for j in range(4)] for i in range(4)])
    for i in range(4):
        for j in range(4):
            if (i + 1, j + 1) in d.keys():
                confusion_mat[i][j] = d[(i + 1, j + 1)]
            else:
                confusion_mat[i][j] = 0.
    print("Confusion Matrix:")
    for row in confusion_mat:
        for col in row:
            print("{:8.3f}".format(col), end=" ")
        print("")

    precision = [confusion_mat[i][i] / dont_be_zero(sum(confusion_mat[i, :])) for i in range(4)]
    recall = [confusion_mat[i][i] / dont_be_zero(sum(confusion_mat[:, i])) for i in range(4)]
    f1 = [2 * (precision[i] * recall[i]) / dont_be_zero((precision[i] + recall[i])) for i in range(4)]
    accuracy = sum([confusion_mat[i][i] for i in range(4)]) / dont_be_zero(
        sum([sum(confusion_mat[i, :]) for i in range(4)]))

    print('precision:', precision, '\tmean precision:', np.mean(precision))
    print('recall:', recall, '\tmean recall:', np.mean(recall))
    print('f1:', f1, '\tmean f1:', np.mean(f1))
    print('accuracy:', accuracy)


evaluation(predictions, test_real_classes)
