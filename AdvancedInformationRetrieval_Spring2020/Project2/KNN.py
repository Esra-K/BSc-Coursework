import json
import codecs
from collections import defaultdict
from math import log, sqrt
import numpy as np
from collections import Counter
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, LancasterStemmer
from nltk.corpus import stopwords

stemmer = LancasterStemmer()
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


train_set = read_json('train.txt')
test_set = read_json('test.txt')


train_set = train_set[:len(train_set) // 2]
test_set = test_set[:len(test_set) // 2]


def dict_level_two():
    return defaultdict(int)


def dict_level_one():
    return defaultdict(dict_level_two)


def process(raw_text):
    punctuations = "!@#$%^&?<>*()[}{]-=/|~`+_'.,:;؛،\؟«»ٰ'\"\\\t\n"
    text = raw_text
    for p in punctuations:
        text = text.replace(p, " ")
    return [x for x in text.split(" ") if not x == '']


word_dict = defaultdict(dict_level_one)
train_classes = [0 for _ in range(len(train_set))]

fancy = 0
weight = 5
for i, element in enumerate(train_set):
    if fancy == 1:
        title_words = fancy_process(element['title'])
        body_words = fancy_process(element['body'])
    else:
        title_words = process(element['title'])
        body_words = process(element['body'])
    data_class = element['category']

    train_classes[i] = data_class
    for word in title_words:
        word_dict[word]['train'][i] += weight

    for word in body_words:
        word_dict[word]['train'][i] += 1

test_classes = [0 for _ in range(len(test_set))]
for i, element in enumerate(test_set):
    if fancy == 1:
        title_words = fancy_process(element['title'])
        body_words = fancy_process(element['body'])
    else:
        title_words = process(element['title'])
        body_words = process(element['body'])
    data_class = element['category']

    test_classes[i] = data_class
    for word in title_words:
        word_dict[word]['test'][i] += weight

    for word in body_words:
        word_dict[word]['test'][i] += 1


def most_common(lst):
    return max(set(lst), key=lst.count)


vectors = [[0. for j in range(len(train_set))] for i in range(len(test_set))]
idf_dict = {term: log((1 + len(train_set) + len(test_set)) /
                      (1 + len(list(word_dict[term]['train'].keys()))
                       + len(list(word_dict[term]['test'].keys())))) for term in word_dict}
method = 'euclidean_distance'

if method == 'cosine':
    terms = list(word_dict.keys())
    test_norms = [0. for i in range(len(test_set))]
    train_norms = [0. for i in range(len(train_set))]
    for term, term_dict in word_dict.items():
        idf = idf_dict[term] ** 2
        train_docs = term_dict['train']
        test_docs = term_dict['test']
        for i, freq_train in train_docs.items():
            train_norms[i] += (freq_train ** 2) * idf
        for i, freq_test in test_docs.items():
            test_norms[i] += (freq_test ** 2) * idf
        for i, freq_test in test_docs.items():
            for j, freq_train in train_docs.items():
                vectors[i][j] += freq_train * freq_test * idf

    train_norms = list(map(sqrt, train_norms))
    test_norms = list(map(sqrt, test_norms))

    for i in range(len(vectors)):
        for j in range(len(vectors[i])):
            vectors[i][j] /= max(2**-15, train_norms[j]) * max(2**-15, test_norms[i])

elif method == 'euclidean_distance':
    for term, term_dict in word_dict.items():
        idf = idf_dict[term] ** 2
        train_docs = term_dict['train']
        test_docs = term_dict['test']
        for i, term_freq in test_docs.items():
            for j in range(len(train_set)):
                vectors[i][j] += term_freq * idf
        for j, term_freq in train_docs.items():
            for i in range(len(test_set)):
                vectors[i][j] += term_freq * idf
        for i, term_freq1 in test_docs.items():
            for j, term_freq2 in train_docs.items():
                vectors[i][j] -= 2 * term_freq1 * term_freq2 * idf
        # print(term)


with open('vectors.txt', 'w') as file:
    file.writelines('\t'.join(str(j) for j in i) + '\n' for i in vectors)


def most_common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


k = 3
predictions = [0 for i in range(len(test_set))]
acc = 0
for i in range(len(vectors)):
    if method == 'euclidean_distance':
        top_k = np.argpartition(vectors[i], k)[:k]
    else:
        top_k = np.argpartition(vectors[i], -1 * k)[-1 * k:]
    top_classes = [train_classes[j] for j in top_k]
    predictions[i] = most_common(top_classes)
    if predictions[i] == test_classes[i]:
        # print("hurray!")
        acc += 1

# print(acc / len(test_classes))
# K = 3 77.77% for euclidean, 78.23% for cosine
# K = 5


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


evaluation(predictions, test_classes)