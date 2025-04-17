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

o1, o2 = map(int, input().split())
dsu = DisjointSet(o1 + 1)
last = [0]*(o1 + 1)
for i in range(o2):
    a = input().split()
    n1 = min(int(a[1]), int(a[2]))
    n2 = max(int(a[1]), int(a[2]))
    if(a[0] == 'normal'):
        dsu.union(dsu.nodes[n1], dsu.nodes[n2])
    elif(a[0] == 'zarbati'):
        mid = (n1 + n2) // 2
        b = n1
        while(b <= n2):
            if(last[b] != 0):
                dsu.union((dsu.nodes[b]) , dsu.nodes[mid])
                k = last[b] + 1
                last[b] = max(last[b], n2)
                b = k
            else:
                dsu.union(dsu.nodes[b], dsu.nodes[mid])
                last[b] = n2
                b += 1
    else:
        if(dsu.find(dsu.nodes[n1]) == dsu.find(dsu.nodes[n2])):
            print("Branko")
        else:
            print("Schafer")


