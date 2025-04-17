destination, capacity, n = map(int, input().split())
arr = []
for i in range(n):
    gas = list(map(int, input().split()))
    arr.append(gas)
arr = sorted(arr, key=lambda x: x[0])
gas = capacity
cost = 0
s = [0] * n
nextSmall = [0] * n
stacklen = 0
for i in range(n - 1, -1, -1):
    while(stacklen > 0 and arr[s[stacklen - 1]][1] >= arr[i][1]):
        stacklen -= 1
    nextSmall[i] = -1 if stacklen == 0 else s[stacklen - 1]
    s[stacklen] = i
    stacklen += 1
gas -= arr[0][0]
flag = False
for i in range(n):
    #print(gas)
    #print(cost)
    if gas < 0:
        print(-1)
        flag = True
        break
    else:
        required = min(capacity, (destination if nextSmall[i] == -1 else arr[nextSmall[i]][0]) - arr[i][0])
        if (required > gas):
            cost += (required - gas) * arr[i][1]
            gas = required
        gas -= (destination if i == n - 1 else arr[i + 1][0]) - arr[i][0]
if not flag:
    if(gas < 0):
        print(-1)
    else:
        print(cost)