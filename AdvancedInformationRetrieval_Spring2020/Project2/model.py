from typing import List, Dict
from collections import defaultdict, Counter
from math import log
from nltk import word_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import operator
stemmer = SnowballStemmer('english')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']',
                   '{', '}', '!', '@', '#', '$', '%', '^', '&', '?', '<', '>'
                   '*', '-', '+', '/', '\\', '_', ''])

fanciness_decoder = [False, False, False]


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


def process(raw_text):
    punctuations = "!@#$%^&?<>*()[}{]-=/|~`+_'.,:;؛،\؟«»ٰ'\"\\\t\n"
    text = raw_text
    for p in punctuations:
        text = text.replace(p, " ")
    return [x for x in text.split(" ") if not x == '']


def dict_level_one_int():
    return defaultdict(float)


word_dict = defaultdict(dict_level_one_int)
class_counts = defaultdict(int)
fancy = 0
weight = 5
idf = defaultdict(float)
D = 0
idf_dict = defaultdict(float)


def train(training_docs: List[Dict]):
    global word_dict, class_counts, fancy, weight, idf
    for i, element in enumerate(training_docs):
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
    global idf_dict, D
    D = len(training_docs)
    idf_dict = {term: log((1 + D) / (1 + idf[term])) for term in word_dict.keys()}
    for term, classes in word_dict.items():
        for c in classes.keys():
            word_dict[term][c] *= idf_dict[term]



def classify(element: Dict) -> int:
    test_dict = defaultdict(float)
    if fancy == 1:
        title_words = fancy_process(element['title'])
        body_words = fancy_process(element['body'])
    else:
        title_words = process(element['title'])
        body_words = process(element['body'])

    title_dict = dict(Counter(title_words))
    for key in title_dict.keys():
        title_dict[key] *= weight
    body_dict = dict(Counter(body_words))

    aggregate_dict = {k: title_dict.get(k, 0) + body_dict.get(k, 0)
                      for k in set(title_dict) | set(body_dict)}

    for key in aggregate_dict.keys():
        if key in word_dict.keys():
            test_dict[key] = aggregate_dict[key]

    for term, tf in test_dict.items():
        test_dict[term] *= idf_dict[term]

    sorted_classes = sorted(class_counts.keys())
    alpha = 10.4
    V = len(word_dict)
    all_freq = {c: sum(word_dict[term][c] for term in word_dict.keys()) for c in sorted_classes}
    score = {key: log((class_counts[key] / D)) for key in sorted_classes}
    for term in test_dict.keys():
        for c in sorted_classes:
            score_i = log((word_dict[term][c] + alpha) / (all_freq[c] + alpha * V))
            score[c] += score_i
    predicted = max(score.items(), key=operator.itemgetter(1))[0]
    return predicted


