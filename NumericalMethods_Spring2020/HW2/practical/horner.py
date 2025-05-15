def horner(poly, x):
    result = 0
    for a in poly:
        result = result * x + a
    return result

poly = list(map(int, input("enter polynomial coefficients e.g. 3 5 0 2 for 3 * x^3 + 5 * x^2 + 2\n").split(" ")))
x = int(input("enter x\n"))
print(horner(poly, x))
