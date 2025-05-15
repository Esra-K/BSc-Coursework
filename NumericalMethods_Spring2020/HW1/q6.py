import math
from math import e
import numpy as np

def natural_log(x):
    q = 0
    y = x
    while y >= 1:
        q += 1
        y /= e
        # print("y:", y, "q:", q)
    i = 1
    a = nth_part(i, y)
    # print(a)
    while math.fabs(a) > 10**-6:
        q += a
        i += 1
        a = nth_part(i, y)
        # print("q:", q, "a:", a)
    return q

def nth_part(n, x):
    return ((-1)**(n+1)) * ((x-1) ** n) / n

inp = float(input())
my_log = natural_log(inp)
their_log = np.log(inp)
print("log:" , my_log)
print("error:",  math.fabs(their_log - my_log))