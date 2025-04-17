class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]


    def find(dsu, u):
        if u != u.par:  # here we user path compression trick
            u.par = dsu.find(u.par)
        return u.par

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False
        # merging two components
        u.par = v
        return True

a, b = map(int, input().split())
dsu = DisjointSet(a)
x = 0
for i in range(b):
    n1, n2 = map(int, input().split())
    n1 = n1 - 1
    n2 = n2 - 1
    if(dsu.union(dsu.nodes[n1], dsu.nodes[n2]) == False):
        x = (2 * x + 1) % 1000000009
    print(x)

