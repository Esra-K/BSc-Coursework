import collections
from collections import defaultdict

def simplifyClause(c, a):
        nc = []
        for i in range(len(c)):
            if (c[i] in a):
                return None
            elif not (-1 * c[i] in a):
                nc.append(c[i])
        return nc

def applyAssignment(f, a):
        nf = []
        for i in range(len(f)):
            nc = simplifyClause(f[i], a)
            if not (nc is None):
                nf.append(nc)
        return nf

def cloneAssignment(a):
        na = defaultdict(list)
        for v in a:
            na[v] = True
        return na

def recDPLL(f, a):
    f = applyAssignment(f, a)
    if len(f) == 0:
        return [True, a]
    for i in range(len(f)):
        if (len(f[i]) == 0): return (False, {})
        elif len(f[i]) == 1:
            a = cloneAssignment(a)
            a[f[i][0]] = True
            return recDPLL(f, a)
    a = cloneAssignment(a)
    a[f[0][0]] = True
    ret = recDPLL(f, a)
    if (ret[0]):
        return ret
    del a[f[0][0]]
    a[-f[0][0]] = True
    return recDPLL(f, a)




na = defaultdict(list)
intro = list(map(int, input().split(" ")))
f = []
for k in range(intro[0]):
    clause = list(map(int, input().split(" ")))
    clause = clause[1:len(clause)]
    f.append(clause)
k = recDPLL(f, defaultdict(list))
if k[0]:
    arr = [0] * intro[1]
    #print(k[1])
    for i in range(intro[1]):
        if(k[1][i + 1] == True):
            arr[i] = 1
    for a in arr:
        print(a)
else:
    print("UNSAT")



