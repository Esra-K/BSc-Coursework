def qsortLittle(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsortLittle([x for x in inlist[1:] if x < pivot])
        greater = qsortLittle([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
    
n = int(input())
strings = input().split(" ")
array = [0] * n
for i in range(len(strings)):
    array[i] = int(strings[i])

array1 = qsortLittle(array)

array2 = array1[: len(array1) // 2]
array3 = array1[len(array1) // 2 :]

for i in range(len(array1) // 2):
    array[2 * i] = array3[i]
    array[2 * i + 1] = array2[i]
if(n % 2):
    array[n - 1] = array1[n - 1]
for a in array[: len(array) - 1]:
    print(a, end=" ")
print(array[len(array) - 1])