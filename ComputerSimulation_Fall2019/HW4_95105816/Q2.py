import random
import numpy

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac
# example: convert_to_float('1 1/2') = 1.5

data = []
n = int(input("Enter number of time-lambda pairs:"))
for i in range(n):
    #print("Enter the " + str(i + 1) + ("st" if i == 0 else "nd" if i == 1 else "rd" if i == 2 else "th") + " time and its respective lambda parameter")
    inp = input().split(" ")
    data.append((int(inp[0]), convert_to_float(inp[1])))
#data = [(0 ,1/15), (60 ,1/12), (120 , 1/7), (180 ,1/5),(240,1/8),(300 ,1/10), (360 ,1/15), (420, 1/20), (480, 1/20)]

times = [a[0] for a in data]
parameters = [a[1] for a in data]
t = 0
lambda_star = max(parameters)
n = 0
while t <= times[len(times) - 1]:
    R1 = random.uniform(0,1)
    E = float(-1 * 1/lambda_star) * numpy.log(R1)
    t += E
    R2 = random.uniform(0,1)
    index = numpy.argmax(times > t) - 1
    if R2 <= float(parameters[index])/lambda_star and t <= times[len(times) - 1] :
        print(t)
        n += 1