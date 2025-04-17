def qsortLittle(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsortLittle([x for x in inlist[1:] if x < pivot])
        greater = qsortLittle([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def findMax(start, end, n):
    start = qsortLittle(start)
    end = qsortLittle(end)
    inn = 1
    max = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (start[i] <= end[j]):
            inn += 1
            if (inn > max):
                max = inn
            i+=1
        else:
            inn -= 1
            j+= 1
    return max

n = int(input())
array0 = [0] * n
array1 = [0] * n
for i in range(n):
    k = input().split()
    array0[i] = int(k[0])
    array1[i] = int(k[1])
print(findMax(array0, array1, n))

