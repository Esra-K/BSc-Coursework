import random
print("Enter number of instances required")
n = int(input())
p = 2
a = [0] * p
x1 = [0] * p
m = [0] * p
c = [0] * p
'''m = [2**31, 2**13, 2**17, 2**23, 2**29, 2**11, 2**37, 2**43, 2**47, 2**53]'''
'''c = [1123,5927,119447,7651087,344312819,1254227431,120324777799,6458937397981,95612298206501,5908417483455341]
a = [2**28 + 1, 2**12 + 1, 2**14 + 1, 2**19+1, 2**25+1, 2**9+1, 2**33+1, 2**40+1, 2**40+1, 2**49 + 1]'''
'''for i in range(p):
    x1.append(random.randint(1, m[i] - 1))'''

print("Enter " + str(p) + " a's, x1's, c's and m's (with space in between)")
for i in range(p):
    get = list(map(int, input().split(" ")))
    a[i], x1[i], c[i], m[i] = get[0], get[1], get[2], get[3]


numbers = []
for i in range(0, n):
    sigma = 0
    one = 1
    for j in range(p):
        coefficient = 0
        x1[j] = ((a[j] * x1[j]) + c[j]) % m[j]
        if x1[j] == 0:
            x1[j] = m[j] - 1
        sigma += (one * x1[j])
        one = -1 * one
    sigma = sigma % (m[0] - 1)
    numbers.append(sigma)

print(numbers)
