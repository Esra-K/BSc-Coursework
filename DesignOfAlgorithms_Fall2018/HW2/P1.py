import math
w = int(input())
n = int(input())
coins = list(map(int, input().split()))
arr=[[21 for j in range(w + 1)] for i in range(n + 1)]
for i in range(n+1):
    arr[i][0]= 0
for j in range(w+1):
    arr[0][j]= -1
for i in range(1,n+1):
    for j in range(1,w+1):
        copy = arr[i][j]
        #print(i - 1)
        #time.sleep(0.08)
        if coins[(i - 1) if i - 1 <len(coins) else len(coins) - 1] <= j:
            if j %coins[(i - 1) if i - 1 <len(coins) else len(coins) - 1] == 0:
                arr[i][j]=1
            elif arr[i - 1][j]>=1:
                arr[i][j]=arr[i - 1][j]
            else:
                min = 21
                k=0
                while j - k * coins[i - 1] >= 0:
                    if arr[i - 1][j - k * coins[i - 1]] > 0 and arr[i - 1][j - k * coins[i - 1]]< min:
                        min = arr[i - 1][j - k * coins[i - 1]]
                    k += 1
                if min!= 21:
                    arr[i][j]= min + 1
        if arr[i][j] == copy :
                arr[i][j]=arr[i - 1][j]
print(arr[n][w])
