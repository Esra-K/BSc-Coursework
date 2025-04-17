import numpy as np

def Jacobi(A):
    n = A.shape[0]
    maxit = 331
    epsilon = 10**-20
    pi = np.pi
    count = 0
    eigenValue = np.zeros(n,float)
    eigenVectors = np.zeros((n,n),float)
    for i in range(0,n):
        eigenVectors[i,i] = 1.0
    for count in range(0,maxit):
         s = 0
         for i in range(0,n):
             s += np.sum(np.abs(A[i,(i+1):n]))

         if (s < epsilon):
              for i in range(0,n):eigenValue[i] = A[i,i]
              break

         else:
              limit = s/(n*(n-1)/2.0)
              for i in range(0,n-1):
                   for j in range(i+1,n):
                       if (np.abs(A[i,j]) > limit):
                           denom = A[i,i] - A[j,j]
                           if (np.abs(denom) < epsilon):  #if tan(phi) ~= inf
                               phi = pi/2
                           else:
                               phi = 0.5*np.arctan(2.0*A[i,j]/denom)
                           sine = np.sin(phi)
                           cosine = np.cos(phi)
                           for k in range(i+1,j):
                               store  = A[i,k]
                               A[i,k] = A[i,k]*cosine + A[k,j]*sine
                               A[k,j] = A[k,j]*cosine - store *sine
                           for k in range(j+1,n):
                               store  = A[i,k]
                               A[i,k] = A[i,k]*cosine + A[j,k]*sine
                               A[j,k] = A[j,k]*cosine - store *sine
                           for k in range(0,i):
                               store  = A[k,i]
                               A[k,i] = A[k,i]*cosine + A[k,j]*sine
                               A[k,j] = A[k,j]*cosine - store *sine
                           store = A[i,i]
                           A[i,i] = A[i,i]*cosine*cosine + 2.0*A[i,j]*cosine*sine +A[j,j]*sine*sine
                           A[j,j] = A[j,j]*cosine*cosine - 2.0*A[i,j]*cosine*sine +store *sine*sine
                           A[i,j] = 0.0
                           for k in range(0,n):
                                store = eigenVectors[k,j]
                                eigenVectors[k,j] = eigenVectors[k,j]*cosine - eigenVectors[k,i]*sine
                                eigenVectors[k,i] = eigenVectors[k,i]*cosine + store *sine
    return eigenValue,eigenVectors,count


nlist = [3,4,5,6]

for n in nlist:
    A = np.random.randint(0, 100, size=(n,n))         # matrix of random numbers
    A = 0.5*(A + np.transpose(A))   # symmetrize matrix
    print("Matrix number" , nlist.index(n), ":\n", A)

    ev,U = np.linalg.eig(A)
    print("Numpy.linalg.eig says:\n","eigenvalues = ",ev, "\neigenvectors = \n", U, "\n")

    ev, U, t = Jacobi(A)
    print("Jacobi(A):\n", "eigenvalues = ", ev, "\neigenvectors = \n", U, "\n\n\n\n")



