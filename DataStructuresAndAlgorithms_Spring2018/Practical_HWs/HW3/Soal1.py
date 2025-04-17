
def findFirstGreaterElement(arr, a):
    low = 0
    high = len(arr)
    while(low != high):
        mid = (low + high) // 2
        if(arr[mid] < a):
            low = mid + 1
        else:
            high = mid
    if (high >= len(array)):
        return len(array)
    return high


Input =input().split(" ")
n = int(Input[0])
x = int(Input[1])
k = int(Input[2])
array = []
Input = input().split(" ")
for i in range(n):
    array.append(int(Input[i]))
sum = 0
for element in array:
    d = (element - 1) // x
    first =  findFirstGreaterElement(array, max((d + k) * x, element))
    last =  findFirstGreaterElement(array, max((d + k + 1) * x, element))
    sum += last - first
print(sum)