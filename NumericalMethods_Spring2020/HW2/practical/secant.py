from math import *


def f(x):
    global string
    return eval(string)

def next(x1, x0):
    return x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))

string = input("enter function\n")
epsilon = eval(input("enter minimum error\n"))

xArray = [-0.75, 4]

while fabs(xArray[-1] - xArray[-2]) >= epsilon:
    a = next(xArray[-1], xArray[-2])
    xArray += [a]

print("answer: ", xArray[-1])
print()
print("error:", f(xArray[-1]))


