from math import *


def euler(f, xn, x0, y0, h):
    n = int((xn - x0) / h)
    if xn < x0:
        h = -1 * h
        n = -1 * n
    x = x0
    y = y0

    for i in range(n):
        y += h * f(x, y)
        print((i + 1), float("{:.4f}".format(y)))
        x += h
    return y


def euler2(f, xn, x0, y0, z0, h):
    n = int((xn - x0) / h)
    if xn < x0:
        h = -1 * h
        n = -1 * n
    x = x0
    y = y0
    z = z0

    for i in range(n):
        yp = y
        y += h * z
        print(i + 1, float("{:.4f}".format(y)))
        z += h * f(x, yp, z)
        x += h
    return y


k = int(input("Enter 1 for 1st order ODE, 2 for 2nd Order ODE\n"))

if k == 1:
    s = "lambda x, y: "
    f_global = input("Enter function for y\':\n")
    xn_global = float(input("Enter x for which value of function is required:\n"))
    x0_global = float(input("Enter x0 (x of initial point):\n"))
    y0_global = float(input("Enter y0 (y of initial point):\n"))
    h_global = float(input("Enter h:\n"))
    yn = euler(eval(s + f_global), xn_global, x0_global, y0_global, h_global)
    print("The value at", xn_global, "is", float("{:.4f}".format(yn)))

if k == 2:
    s = "lambda x, y, z: "
    f_global = input("Enter function for y\" (Important: use z in place of y\") :\n")
    xn_global = float(input("Enter x for which value of function is required:\n"))
    x0_global = float(input("Enter x0 (x of initial point):\n"))
    y0_global = float(input("Enter y0 (y of initial point):\n"))
    z0_global = float(input("Enter y\'0 (y\' of initial point):\n"))
    h_global = float(input("Enter h:\n"))
    yn = euler2(eval(s + f_global), xn_global, x0_global, y0_global, z0_global, h_global)
    print("The value at", xn_global, "is", float("{:.4f}".format(yn)))
