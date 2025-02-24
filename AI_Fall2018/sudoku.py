def print1(arr):
    for i in range(4):
        for j in range(4):
            if(j < 3):
                print(arr[i][j], end=' ')
            elif(i < 3):
                print(arr[i][j])
            else:
                print(arr[i][j], end='')

def find(arr, l):
    for row in range(4):
        for col in range(4):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

def usedInRow(arr, row, num):
    for i in range(4):
        if (arr[row][i] == num):
            return True
    return False

def usedInColumn(arr, col, num):
    for i in range(4):
        if (arr[i][col] == num):
            return True
    return False

def usedInSubsquare(arr, row, col, num):
    for i in range(2):
        for j in range(2):
            if (arr[i + row][j + col] == num):
                return True
    return False

def isSatisfying(arr, row, col, num):
    return not usedInRow(arr, row, num) and not usedInColumn(arr, col, num) and not usedInSubsquare(arr, row - row % 2,
                                                                                                 col - col % 2, num)

def solve(arr):
    l = [0, 0]
    if (not find(arr, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 5):
        if (isSatisfying(arr, row, col, num)):
            arr[row][col] = num
            if (solve(arr)):
                return True
            arr[row][col] = 0
    return False

a = [[0]*4]*4
#print(a)
for i in range(4):
    get = list(map(int, input().split()))
    a[i] = get
#print(a)
if(solve(a)):
    print1(a)
else:
    print1(-1)
