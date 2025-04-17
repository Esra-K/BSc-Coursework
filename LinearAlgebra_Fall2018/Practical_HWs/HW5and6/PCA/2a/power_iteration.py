from random import normalvariate
import numpy as np
from numpy.dual import norm
from math import sqrt
from PIL import Image
import matplotlib.pyplot as plt
import time

def random_unit_vector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    the_norm = sqrt(sum(x * x for x in unnormalized))
    return [x / the_norm for x in unnormalized]


def first_pc(a):
    epsilon = 1e-10
    a = np.array(a, dtype=float)
    cov = a.dot(a.T)
    n = cov.shape[0]
    x = random_unit_vector(n)
    current_v = x

    while True:
        last_v = current_v
        current_v = np.dot(cov, last_v)
        current_v = current_v / norm(current_v)

        if abs(np.dot(current_v, last_v)) > 1 - epsilon:
            return current_v


# reading the image
img = Image.open('sample.jpg')
imggray = img.convert('LA')
# file1 = open("written.txt","w")
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
# print(imgmat.shape)
# for k in imgmat.tolist():
#     file1.write(str(k))
# file1.close()

start_time = time.time()

v = first_pc(imgmat)
#print(len(v))

basisMatrix = np.empty((0,836), dtype=float)

basisMatrix = np.vstack((basisMatrix, v))
#print(basisMatrix.shape)
basisMatrixT = np.transpose(basisMatrix)
#print(basisMatrixT.shape)
operator = np.matmul(basisMatrixT, basisMatrix)
#print(operator.shape)
projection = np.matmul(operator,imgmat)
imgmat2 = np.subtract(imgmat, projection)
i = 1

for j in range(2, 51):
    v = first_pc(imgmat2)
    basisMatrix = np.vstack((basisMatrix, v))
    #print(len(basisMatrix))
    basisMatrixT = np.transpose(basisMatrix)
    operator = np.matmul(basisMatrixT, basisMatrix)
    projection = np.matmul(operator, imgmat)
    imgmat2 = imgmat - projection

    if j % 10 == 0:
        ax = plt.subplot(2, 3, i, frame_on=False)
        ax.xaxis.set_major_locator(plt.NullLocator())  # remove ticks
        ax.yaxis.set_major_locator(plt.NullLocator())
        i += 1
        plt.imshow(np.flipud(projection), origin='lower')
        plt.title('PCs # ' + str(j))
        plt.gray()
    if (j == 50):
        difference = 0
        for m in range(len(projection)):
            for n in range(len(projection[m])):
                difference += abs(projection[m][n] - imgmat[m][n])
        print("Total difference of entries:", difference)
print("Time elapsed using power iteration method: %s seconds" % (time.time() - start_time))
plt.show()
        # showing the image
        # plt.style.use('classic')
        # plt.imshow(projection, cmap='gray')
        # title = "Image projection with N=" + str(j)
        # plt.title(title)
        # plt.show()