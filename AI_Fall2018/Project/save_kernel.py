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
# for datum in data:
#     print(data)
print("data.shape",data.shape)
data = np.array(data)


# image = np.asarray(data[len(data) - 1]).squeeze()
# print("len(data)", len(data))
# print(image)
# plt.imshow(image)
# plt.show()
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

kernel = []
for i in range(10):
    temp = []
    for j in range(num_images):
        temp.append(0)
    kernel.append(temp)



print(data.shape)
print(data)

start = time.time()
for k in range(len(data)):
    classOfKthDatum = [0] * 10
    for i in range(len(kernel)):
        scoreOfI = 0
        for j in range(len(kernel[i])):
            similarity = kernel[i][j]*((1 + np.dot(data[k],data[j]))**5) # (np.exp((-1) * (np.linalg.norm(np.subtract(data[k], data[j])))))
            scoreOfI += similarity
        classOfKthDatum[i] = scoreOfI
    allMaxGuys = [x for x, y in enumerate(classOfKthDatum) if y == max(classOfKthDatum)]
    optimal = labels[k]
    if len(allMaxGuys) == 1 and allMaxGuys[0] == optimal:
        continue
    else:
        kernel[optimal][k] += 1
        for mistakes in allMaxGuys:
            if mistakes != optimal :
                kernel[mistakes][k] -= 1


end = time.time()
print(end - start)

np.save('Kernel', kernel)
