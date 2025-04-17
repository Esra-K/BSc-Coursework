import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time


img = Image.open('sample.jpg')
imggray = img.convert('LA')
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])


start_time = time.time()

U, sigma, V = np.linalg.svd(np.array(imgmat))
j = 1
for i in range(10, 51, 10):
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    ax = plt.subplot(2, 3, j, frame_on=False)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    j += 1
    plt.imshow(np.flipud(reconstimg), origin='lower')
    plt.title('PCs # ' + str((j-1)*10))
    plt.gray()
    if(i == 50):
        difference = 0
        o = np.array(reconstimg)
        for m in range(len(o)):
            for n in range(len(o[m])):
                difference += abs(o[m][n] - imgmat[m][n])
        print("Total difference of entries:" ,difference)

print("Time elapsed using svd method: %s seconds" % (time.time() - start_time))
plt.show()