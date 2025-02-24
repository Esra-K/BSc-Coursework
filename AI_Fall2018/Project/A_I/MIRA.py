import numpy as np
import random
import gzip
import time



imagesize = 28
imagelength = imagesize * imagesize

labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

Xfile = "data/train-images-idx3-ubyte.gz"
yfile = "data/train-labels-idx1-ubyte.gz"
vXfile = "data/t10k-images-idx3-ubyte.gz"
vyfile = "data/t10k-labels-idx1-ubyte.gz"

trainingdatalength = None
validationdatalength = None

showvalidationerrors = True


enable_sampler = False


input_size = imagelength
hidden_size = 784
output_size = len(labels)


batchsize = 10
epochs = 10
softloss = 0.01
outputinterval = 25
multiline_status = True

# TRAINING DATA SETUP
print("Initializing training and validation data ...", end="", flush=True)

with gzip.open(yfile) as bytestream:
    if not trainingdatalength:
        bytestream.read(4)
        trainingdatalength = int.from_bytes(bytestream.read(4), 'big')
    else:
        bytestream.read(8)

    buf = bytestream.read(trainingdatalength)
    y = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    y = y.reshape(trainingdatalength, 1)
    tempy = []
    for y_i in y:
        temp = [0.0] * len(labels)
        temp[int(y_i)] = 1.0
        tempy += temp

    y = np.array(tempy)
    y = y.reshape(trainingdatalength, len(labels))

with gzip.open(Xfile) as bytestream:
    bytestream.read(16)
    buf = bytestream.read(imagelength * trainingdatalength)
    X = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    X = X / 255.0
    X = X.reshape(trainingdatalength, imagelength)

with gzip.open(vyfile) as bytestream:
    if not validationdatalength:
        bytestream.read(4)
        validationdatalength = int.from_bytes(bytestream.read(4), 'big')
    else:
        bytestream.read(8)

    buf = bytestream.read(validationdatalength)
    vy = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    vy = vy.reshape(validationdatalength, 1)
    tempvy = []
    for vy_i in vy:
        temp = [0.0] * len(labels)
        temp[int(vy_i)] = 1.0
        tempvy += temp
    vy = np.array(tempvy)
    vy = vy.reshape(validationdatalength, len(labels))


with gzip.open(vXfile) as bytestream:
    bytestream.read(16)
    buf = bytestream.read(imagelength * validationdatalength)
    vX = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    vX = vX / 255.0
    vX = vX.reshape(validationdatalength, imagelength)


print(" complete")


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def dsigmoid(s):
    return s * (1 - s)


def tanh(s):
    return np.tanh(s)


def dtanh(s):
    return 1.0 - (np.tanh(s) ** 2)


def softmax(s):
    exps = np.exp(s - np.max(s, axis=-1, keepdims=True))
    return exps / np.sum(exps, axis=-1, keepdims=True)


def crossentropy(y, y_, e=1e-12):
    return -np.sum(y * np.log(y_ + e))


def batchtostring(batch):
    string = ""
    for y in batch:
        n = np.argmax(y)
        string += "%s %s\n" % (labels[n], str(np.round(y, 2)))
    return string



class mira:

    def __init__(self, N=2, H=3, O=1):
        self.N = N
        self.H = H
        self.O = O

        self.W1 = np.random.randn(N, H) / np.sqrt(N)
        self.B1 = np.zeros(H)
        self.W2 = np.random.randn(H, H) / np.sqrt(H)
        self.B2 = np.zeros(H)
        self.W3 = np.random.randn(H, O) / np.sqrt(O)
        self.B3 = np.zeros(O)


    def forward(self, X):
        self.z = self.B1 + np.dot(X, self.W1)
        self.z2 = tanh(self.z)
        self.z3 = self.B2 + np.dot(self.z2, self.W2)
        self.z4 = tanh(self.z3)
        self.z5 = self.B3 + np.dot(self.z4, self.W3)
        return softmax(self.z5)

    def backward(self, X, y, o):
        self.o_derror = o - y

        self.z4_error = self.o_derror.dot(self.W3.T)
        self.z4_derror = self.z4_error * dtanh(self.z4)

        self.z2_error = self.z4_derror.dot(self.W2.T)
        self.z2_derror = self.z2_error * dtanh(self.z2)

        dW1 = X.T.dot(self.z2_derror)
        dB1 = np.sum(self.z2_derror, axis=0)
        dW2 = self.z2.T.dot(self.z4_derror)
        dB2 = np.sum(self.z4_derror, axis=0)
        dW3 = self.z4.T.dot(self.o_derror)
        dB3 = np.sum(self.o_derror, axis=0)
        return dW1, dB1, dW2, dB2, dW3, dB3

    def train(self, X, y, batchsize, alpha=1):
        o = self.forward(X)
        dW1, dB1, dW2, dB2, dW3, dB3 = self.backward(X, y, o)

        self.W1 += -alpha * dW1
        self.B1 += -alpha * dB1
        self.W2 += -alpha * dW2
        self.B2 += -alpha * dB2
        self.W3 += -alpha * dW3
        self.B3 += -alpha * dB3

        return o


mp = mira(imagelength, hidden_size, len(labels))


forward = mp.forward(X[0:batchsize])
indicatedloss = crossentropy(y[0:batchsize], forward) / batchsize
averageloss = indicatedloss

starttime = time.time()
c = 0.002

error = False
tau = 0.001

for e in range(0, epochs):
    try:
        epoch_startloss = averageloss
        averageloss = 0.0

        print("Shuffling...\r", end="", flush="True")
        indices = np.arange(X.shape[0])

        np.random.shuffle(indices)

        X = X[indices]
        y = y[indices]

        iterations = int(X.shape[0] / batchsize)

        for i in range(0, iterations):

            forward = mp.train(X[i:i+1], y[i:i+1], batchsize, tau)


            if (np.argmax(forward) != np.argmax(y[i:i+1])):
                tau = (abs(np.dot((mp.W2[np.argmax(forward)] - mp.W2[np.argmax(y[i:i+1])]) ,X[i:i+1][0].tolist())) +1 ) / np.dot(X[i:i+1][0],X[i:i+1][0])
                #print(tau)

            loss = crossentropy(y[i:i+1], forward)
            averageloss += loss
            f = X[i:i+1][0]*tau

            indicatedloss = loss * softloss + (1 - softloss) * indicatedloss

            if i % outputinterval == 0 or i + 1 == iterations:
                print('\rEpoch %03d Loss: %.5f tau: %.5f ...  %.2f%%' %
                      (e,
                       indicatedloss if i + 1 != iterations else averageloss / (1.0 * trainingdatalength / batchsize),
                       tau,
                       (i + 1) / iterations * 100.0),
                      end="", flush=True)
        if multiline_status:
            print(" complete")


        averageloss /= 1.0 * trainingdatalength / batchsize


    except KeyboardInterrupt:
        error = True
        print(' aborted')
        break


# print(type(mp.W1))
# np.save("miraW1", mp.W1)
# np.save("miraW2",mp.W2)
# np.save("miraW3",mp.W3)
# np.save("miraB1",mp.B1)
# np.save("miraB2",mp.B2)
# np.save("miraB3",mp.B3)

# print(type(mp.W1))
# mp.W1 = np.load("miraW1.npy")
# mp.W2 = np.load("miraW2.npy")
# mp.W3 = np.load("miraW3.npy")
# mp.B1 = np.load("miraB1.npy")
# mp.B2 = np.load("miraB2.npy")
# mp.B3 = np.load("miraB3.npy")
#


if not error:
    print(" complete")
print("Trained %i epochs on %i samples in %.2f seconds \n" % (epochs, trainingdatalength, time.time() - starttime))

print("Validating...\r", end="", flush="True")
errors = 0
for i in range(0, validationdatalength):
    prediction = mp.forward(vX[i:i + 1])

    if np.argmax(prediction) != np.argmax(vy[i]):
        errors += 1

print("Validation: %i out of %i - %.2f%%" % (
validationdatalength - errors, validationdatalength, (100.0 * (validationdatalength - errors) / validationdatalength)))

