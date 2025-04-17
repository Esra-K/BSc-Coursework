from collections import defaultdict
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]

def BFS(g, u, n):
    visited = [False] * n
    distance = [0] * n
    q = Queue(n)
    q.enqueue(u)
    visited[u] = True
    while q.num != 0:
        x = q.dequeue()
        for i in range(len(g[x])):
            if(visited[g[x][i]] == True):
                continue
            distance[g[x][i]] = distance[x] + 1
            q.enqueue(g[x][i])
            visited[g[x][i]] = True
    '''for i in range(len(distance)):
        print("distance of " + str(u) + " from " + str(i) + " is: " + str(distance[i]) )'''
    return max(distance)







n, m = map(int, input().split())
G = defaultdict(list)
for i in range(m):
    s, t = map(int, input().split())
    G[s - 1].append(t - 1)
    G[t - 1].append(s - 1)

# print(G)
maxi = 0
for i in range(n):
    if maxi < BFS(G, i, n):
        maxi = BFS(G, i, n)
        # print(i, BFS(G, i, n))

print(maxi)



