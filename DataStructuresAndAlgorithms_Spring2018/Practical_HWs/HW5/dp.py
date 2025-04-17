n = int(input())
g = [[0 for i in range(n+ 1)] for j in range(n + 1)]
g[0][0] = 1
s = input()
for k in range(1,n + 1):
    for l in range(0, min(k + 1, n)):
        if s[k - 1] == '(':
            if l > 0:
                g[k][l] = g[k - 1][l - 1] + g[k - 1][l + 1]
            else:
                g[k][l] = g[k - 1][l + 1]
        else:
            g[k][l] = g[k - 1][l + 1]
# print(g)
print(g[n][0])