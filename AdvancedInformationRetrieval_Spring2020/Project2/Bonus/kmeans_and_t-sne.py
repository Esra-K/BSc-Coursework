import json
import codecs
from collections import defaultdict
from math import log, sqrt, pi, e
from collections import Counter
from copy import deepcopy
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
from sklearn.manifold import TSNE


def fashion_scatter(x, colors):
    num_classes = len(np.unique(colors))
    palette = np.array(sns.color_palette("hls", num_classes))

    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40, c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

    txts = []

    for i in range(num_classes):

        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()])
        txts.append(txt)
    plt.show()
    return f, ax, sc, txts


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


set2 = get_term_set('test.txt', subset_index=2)
x_test, y_test = get_dataset(set2, 'test.txt', weight=5, subset_index=2)
x_test = x_test / np.linalg.norm(x_test, axis=1, keepdims=True)

k = 4
m = x_test.shape[0]
n = x_test.shape[1]
mean = np.mean(x_test, axis=0)
std = np.std(x_test, axis=0)
# random_centers = np.random.randn(k, n) * std + mean
old_centroids = np.zeros((k, n))
new_centroids = np.random.randn(k, n) * std + mean # deepcopy(random_centers)
clusters = np.zeros(m)
distances = np.zeros((m, k))
centroid_difference = np.linalg.norm(new_centroids - old_centroids)

while centroid_difference != 0.:
    for i in range(k):
        distances[:, i] = np.linalg.norm(x_test - new_centroids[i], axis=1)
    clusters = np.argmin(distances, axis=1)
    old_centroids = deepcopy(new_centroids)
    for i in range(k):
        new_centroids[i] = np.mean(x_test[clusters == i], axis=0)
    centroid_difference = np.linalg.norm(new_centroids - old_centroids)

kmeans = KMeans(n_clusters=4, random_state=937).fit(x_test)

print(dict(Counter(clusters)))
print(dict(Counter(y_test)))


sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})
RS = 123

x_subset = x_test[0:200]
y_subset = clusters[0:200]
y_builtin = kmeans.labels_
print('here')
# print(np.unique(y_subset))

fashion_tsne = TSNE(random_state=RS).fit_transform(x_test)
fashion_scatter(fashion_tsne, clusters)
fashion_scatter(fashion_tsne, y_builtin)
