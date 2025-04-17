class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def maxHist(R, C, row):
    result = Stack()
    max_area = 0
    area = 0
    i = 0
    while (i < C):
        if (result.empty() or row[result.peek()] <= row[i]):
            result.push(i)
            i+=1
        else:
            top_val = row[result.peek()]
            result.pop()
            area = top_val * i
            if (result.empty()== False):
                area = top_val * (i - result.peek() - 1 )
            max_area = max(area, max_area)

    while (result.empty() == False):
        top_val = row[result.peek()]
        result.pop()
        area = top_val * i
        if (result.empty() == False):
            area = top_val * (i - result.peek() - 1 )
        max_area = max(area, max_area)

    return max_area


def Bigrec(row, column, matrix):
    result = maxHist(row, column, matrix[0])
    for i in range(1,row):
        for j in range(column):
            if (matrix[i][j] == 1):
                matrix[i][j] += matrix[i - 1][j]
        result = max(result, maxHist(row, column, matrix[i]))
    return result



prompt = input().split(" ")
#print(prompt)
nrows = int(prompt[0])
ncols = int(prompt[1])
a = [[0 for x in range(ncols)] for y in range(nrows)]
for i in range(nrows):
    row = list(input())
    j = 0
    for k in row :
        if(k == '.'):
            a[i][j] = 1
        else:
            a[i][j] = 0
        j+=1
print(Bigrec(nrows,ncols, a))
