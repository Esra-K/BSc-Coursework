import gzip
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
np.set_printoptions(threshold=sys.maxsize)
import time

f = gzip.open('train-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 5000


f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size* image_size)
data = np.array(data)

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
a = f2.read(8)
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
kernel = np.load('Kernel.npy')
start = time.time()
for k in range(len(data2)):
    classOfKthDatum = [0] * 10
    for i in range(len(kernel)):
        scoreOfI = 0
        for j in range(len(kernel[i])):
            similarity = kernel[i][j]*((1 + np.dot(data2[k],data[j]))**5) # (np.exp((-1) * (np.linalg.norm(np.subtract(data2[k], data[j])))))
            scoreOfI += similarity
        classOfKthDatum[i] = scoreOfI
    allMaxGuys = [x for x, y in enumerate(classOfKthDatum) if y == max(classOfKthDatum)]
    optimal = test_labels[k]
    if len(allMaxGuys) == 1 and allMaxGuys[0] == optimal:
        true += 1
    else:
        false += 1

    if((k + 1) % 500 == 0):
        print("Results for ", k + 1, "test samples:")
        print("true", true)
        print("false", false)
        print("success rate:", (float(true) * 100) / (true + false))
        end = time.time()
        print(end - start)
        start = time.time()

print("true", true)
print("false", false)
print("success rate:", ( float(true) * 100)/(true + false))
end = time.time()
print(end - start)
