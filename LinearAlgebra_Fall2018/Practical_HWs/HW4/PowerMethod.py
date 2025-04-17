import numpy as np
import math
n = 3
epsilon = 10**-6
iterationLimit = 331
arr = np.array([[-100, 3, 5], [7, 6, 5], [7, 8, 9]])
vector = np.random.randint(0,100,size=n)
vector = [a/math.fabs(max(vector, key=abs)) for a in vector]

norm = 0
count = 0
while count < iterationLimit:
    print("stage", count,":\neigenvalue: ", norm, "eigenvector: ", vector)
    z = arr.dot(vector)
    norm = max(z, key=abs)
    z = [a/math.fabs(norm) for a in z]
    sigma = 0.
    for i in range(len(z)):
        sigma = sigma + (z[i] - vector[i])**2
    sigma = sigma/len(z)
    sigma = math.sqrt(sigma)
    if (sigma < epsilon):
        break
    vector = [a for a in z]
    count +=1


print("eigenvalue: ",norm , "eigenvector: ", vector, "number of iterations:", count)

mat = np.matrix(arr)
u,v = np.linalg.eig(mat)
print("Our precise maximum eigenvalue is",max(u, key=abs))

#مقدار ویژه کوچکتر
bigLambda = norm
arr2 = arr.copy()
epsilon = 10**-10
for i in range(len(arr)):
    arr[i][i] -= bigLambda
vector = np.random.randint(1,100,size=n)
vector = [a/math.fabs(max(vector, key=abs)) for a in vector]
z = [0] * n
norm = 0
count = 0
while count < iterationLimit:
    z = arr.dot(vector)
    norm = max(z, key=abs)
    z = [a/math.fabs(norm) for a in z]
    sigma = 0.
    for i in range(len(z)):
        sigma = sigma + (z[i] - vector[i])**2
    sigma = sigma/len(z)
    sigma = math.sqrt(sigma)
    if (sigma < epsilon):
        break
    vector = [a for a in z]
    count +=1
print("\n\n Part 3:\neigenvalue:" , norm + bigLambda, "eigenvector:" , vector )

