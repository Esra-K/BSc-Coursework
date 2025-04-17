from collections import defaultdict
def do(arr, dic, u, v):
    arr[u] = 1
    for i in range(len(dic[u])):
        if(dic[u][i] == v):
            continue
        do(arr, dic,dic[u][i],u)
        arr[u] += arr[dic[u][i]]
    return arr
n = int(input())
d = defaultdict(list)
c = [0] * (n + 1)
for i in range(n - 1):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
c = do(c, d, 1, 0)
odd, even = 0,0

for i in range(1, n + 1):
    odd, even = (odd + (c[i] + 1) % 2), (even + c[i] % 2)
print(even, odd)

