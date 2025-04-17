n, m = map(int, input().split())
credit = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())
    credit[a] , credit[b] = credit[a] - c, credit[b] + c
print(sum(credit[i] for i in range(n) if credit[i] > 0))
