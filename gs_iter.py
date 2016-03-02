# Gauss-Seidel Iterative Method
# function takes in a 3x1 vector, tolerance parameter, and positive int M giving the max iterations
# returns approx solution x and number of iterations needed to obtain approx
# Random generate initial vectors

import numpy as np
import matrixMultiplication as mm
import math as math

def gs_iter(x, tol, M):
    x = x.flatten()
    numIter = 0
    U = np.array([[0,1/2,1/3], [0,0,1/4], [0,0,0]], float)
    Linv = np.array([[1,0,0],[-1/2,1,0],[-5/24,-1/4,1]],float)
    b = np.array([0.1,0.1,0.1], float)

    while numIter < M:
        prevX = x
        x = mm.powerMult(Linv, b - mm.powerMult(U, x))
        diff = np.subtract(x,prevX)
        numIter += 1
        if np.max(np.abs(diff)) <= tol:
            return [x, numIter]
    return None






