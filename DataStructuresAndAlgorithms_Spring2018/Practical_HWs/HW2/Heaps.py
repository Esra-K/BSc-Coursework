import sys
sys.setrecursionlimit(1000000)

def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


class Min_Heap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def bubble_up(self, ind):
        while ind > 0 and self.heap[ind] < self.heap[parent(ind)]:
            self.heap[ind], self.heap[parent(ind)] = self.heap[parent(ind)], self.heap[ind]
            ind = parent(ind)

    def bubble_down(self, ind):
        while left_child(ind) < self.size():
            newInd = ind
            if self.heap[left_child(ind)] < self.heap[ind]:
                newInd = left_child(ind)
            if right_child(ind) < self.size() and self.heap[right_child(ind)] < self.heap[newInd]:
                newInd = right_child(ind)
            #dare mige age hichkoodome shooroote bala bargharaar nabood yani elementemoon sare jaye dorosteshe
            if ind == newInd:
                break
            self.heap[ind], self.heap[newInd] = self.heap[newInd], self.heap[ind]
            ind = newInd

    def insert(self, item):
        self.heap = self.heap + [item]
        self.bubble_up(self.size() - 1)

    def inOrder(self, i):
        if i >= self.size() or i < 0:
           return []
        lesser = self.inOrder(left_child(i))
        larger = self.inOrder(right_child(i))
        return lesser + [self.heap[i]] + larger






numbers = int(input())
h = []
for i in range(numbers):
    h.append(int(input()))
heap = Min_Heap()
for a in h:
    heap.insert(a)
h.sort()

k = heap.inOrder(0)
dif = 0
for i in range(len(h)):
    if(h[i] != k[i]):
        dif+=1
print(str(dif))