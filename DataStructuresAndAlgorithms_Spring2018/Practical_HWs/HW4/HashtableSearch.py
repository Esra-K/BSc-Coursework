def hash(s):
    hash1 = [0] * len(s)
    hash1[0] = (s[0])
    hash2 = [0] * len(s)
    hash2[0] = s[len(s) - 1]
    p = 2
    pint = 1
    mod = 10**9 + 7
    for i in range(1, len(s)):
        pint = pint * p
        hash1[i] = (hash1[i - 1] + s[i] * pint) % mod
        hash2[i] = (hash2[i - 1] * p + s[len(s) - 1 - i]) % mod
    return hash1 + hash2

inp = input()
for test in range(int(inp)):
    n, k = map(int, input().split())
    subArray = list(map(int, input().split()))
    index = list(map(int, input().split()))
    bully = False
    h = hash(subArray)
    h0 = h[0: len(h) // 2]
    h1 = h[len(h) // 2: len(h)]
    for element in range(len(subArray)):
        if(subArray[element] > k or subArray[element] < 1 ):
            bully = True
            break
    length = len(subArray)
    if(index[len(index) - 1] + length - 1 > n):
        bully = True
    some = 0
    for e in range(1,len(index)):
        z = index[e] - index[e - 1]
        some += min(length,z)
        #print(e, some)
        z = length - z
        if(z >0):
            if(h0[z - 1] != h1[z - 1] ):
                bully = True
                break

    if(length > n or bully == True):
        print("Case " + str(test + 1) + ": " + str(0))
    else:
        some += length
        some = n - some
        #print(k, some)
        print("Case ".__add__(str(test + 1)).__add__(": ").__add__(str(pow(k, some, 1000000007))))