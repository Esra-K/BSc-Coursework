s = input()
p = 447
h = [0] * len(s)
hh = [0] * len(s)
mod = 10**9 + 7
hh[0] = ord(s[0])
h[0] = ord(s[0])
powerHouse = 1
for i in range(1,len(s)):
    powerHouse = (powerHouse * p) % mod
    h[i] = (ord(s[i]) * powerHouse + h[i - 1]) % mod
    hh[i] = (hh[i - 1] * p + ord(s[i])) % mod
#print(h)
#print(hh)
sum = [0] * len(s)
h = [0] + h
hh = [0] + hh
sum = [0] + sum
some = 0
for i in range(len(hh) - 1):
    if(h[i + 1] == hh[i + 1]):
        sum[i + 1] = 1 + sum[(i + 1)// 2]
        some = some +  sum[i + 1]
print(some)