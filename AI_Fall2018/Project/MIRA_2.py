import gzip
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
np.set_printoptions(threshold=sys.maxsize)
import time
import random

f = gzip.open('train-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 60000


f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size* image_size)
# for datum in data:
#     print(data)
print("data.shape",data.shape)
data = np.array(data)

f = gzip.open('train-labels-idx1-ubyte.gz','r')
labels = []
a = f.read(8)
for i in range(len(data)):
    # a = f.read(8)
    buf = f.read(1)
    labels.append(np.frombuffer(buf, dtype=np.uint8).astype(np.int64))
# buf = f.read()
# print(buf)
labels = list(itertools.chain.from_iterable(labels))
print("len(labels)", len(labels))
print(labels)
for l in range((len(labels))):
    print("labels[l]", labels[l])
    image = np.asarray(data[l]).squeeze()
    #print("len(data)", len(data))
    # print(image)
    # plt.imshow(image)
    # plt.show()
print("len(data)", len(data))

# reference1 = [i for i in range(30000)]
# np.random.shuffle(reference1)
#
# reference2 = [i for i in range(30000, 60000)]
# np.random.shuffle(reference2)
# reference = np.concatenate((reference2, reference1))

features = []
for i in range(10):
    temp = []
    for j in range(28*28):
        temp.append(0)
    features.append(temp)

for numberOfIterations in range(10):
    for i in range(60000):
        realValue = labels[i]
        destined_dot = np.dot(data[i], features[realValue])
        el_normo = np.dot(data[i], data[i])
        for j in range(len(features)):
            if j == realValue:
                continue
            ill_fated_dot = np.dot(data[i], features[j])
            if ill_fated_dot >= destined_dot:
                taw = (np.dot(np.subtract(features[j] , features[realValue]), data[i]) + 1) / (2 * el_normo)
                scalar_mult  = [x * taw for x in data[i]]
                features[j] = np.subtract(features[j], scalar_mult)
                features[realValue] = np.add(features[realValue] , scalar_mult)


np.save('MiraFeatures4', np.array(features))

features = np.load('MiraFeatures4.npy')

f2 = gzip.open('t10k-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 10000


f2.read(16)
buf = f2.read(image_size * image_size * num_images)
data2 = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data2 = data2.reshape(num_images, image_size* image_size)
# for datum in data:
#     print(data)
print("data.shape",data2.shape)

# image = np.asarray(data[len(data) - 1]).squeeze()
# print("len(data)", len(data))
# print(image)
# plt.imshow(image)
# plt.show()
f2 = gzip.open('t10k-labels-idx1-ubyte.gz','r')
test_labels = []
a3= f2.read(8)
for i in range(len(data2)):
    # a = f.read(8)
    buf = f2.read(1)
    test_labels.append(np.frombuffer(buf, dtype=np.uint8).astype(np.int64))
# buf = f.read()
# print(buf)
test_labels = list(itertools.chain.from_iterable(test_labels))
print("len(labels)", len(test_labels))
print(test_labels)
for l in range((len(test_labels))):
    print("labels[", l, "]", test_labels[l])
    image = np.asarray(data2[l]).squeeze()
    #print("len(data)", len(data))
    # print(image)
    # plt.imshow(image)
    # plt.show()
print("len(data)", len(data2))
true = 0
false = 0
start = time.time()
for i in range(len(data2)):
    dotResults = [0] * 10
    for j in range(10):
        dotResults[j] = np.dot(data2[i], features[j])
    optimal = test_labels[i]
    if dotResults[optimal] == max(dotResults):
        true += 1
    else:
        false += 1
    if(i + 1) % 500 == 0:
        print("Results for",i+1,"test samples:")
        print("Success rate:", float(true * 100)/ (true + false))
        end = time.time()
        print("time elapsed:", end - start)
        start = time.time()
