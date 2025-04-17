p = int(input())
p -= 1
if(p == 0):
    print(0)
else:
    a = []
    #profs = 0
    indices = []
    r = input()
    r = r.split(" ")
    for i in range(p):
        if int(r[i]) == 1:
            #profs += 1
            indices += [i]
    #print("len(indices)".__add__(str(len(indices))))
    #print(r)
    #print(indices)
    j = 0
    k = indices[0]
    r = input()
    r = r.split(" ")
    #print(r)
    for i in range(p):
        number = int(r[i])
        #print("number".__add__(str(number)))
        if(i == k):
            a.sort()
            a = a[max(0, len(a) - number + 1): len(a)]
            #print("a alan ine: ".__add__(str(a)))

            #print("k".__add__(str(k)))
            #print("j".__add__(str(j)))
            if(j + 1 < len(indices)):
                j+=1
            k = indices[j]
        else:
            a += [number]
            #print("i ".__add__(str(i)))
    sum = 0
    if(a.__len__() == 0):
        print(0)
    else:
        for b in range(len(a)):
            sum += int(a[b])
        #print(a)
        print(str(sum))
