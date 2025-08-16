# f1 = sqrt(2 * r), f2 = 4 - 2* sqrt(2 * (1 - r))
import random, math
n = int(input("Enter number of instances required"))
exp = []
triangle = []
for i in range(n):
    u = random.uniform(0,1)
    exp.append(float(-1/2) * float(math.log(1 - u)))
    triangle.append(math.sqrt(8 * u) if u <= 0.5 else (4 - 2 * math.sqrt(2 - 2 * u)))
print(exp)
print(triangle)