class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.columns = len(graph[0])

    def bpm(self, u, matchR, seen):
        for v in range(self.columns):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxBPM(self):
        matchR = [-1] * self.columns
        result = 0
        for i in range(self.rows):
            seen = [False] * self.columns
            if self.bpm(i, matchR, seen):
                result += 1
        return result


m, n, k = map(int, input().split(" "))
bpGraph = []
for i in range(m):
    arr = []
    for j in range(n):
        arr.append(1)
    bpGraph.append(arr)

for a in range(k):
    i, j = map(int, input().split(" "))
    bpGraph[i][j] = 0
#print(bpGraph)
g = Graph(bpGraph)
print(g.maxBPM())
