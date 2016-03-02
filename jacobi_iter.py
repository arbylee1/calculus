__author__ = 'Ecclesia'
import numpy as numpy
import matrixMultiplication as matrix

# Jacobi Iterative Method
# function takes in a 3x1 vector, tolerance parameter, and positive int M giving the max iterations
# @return [approx solution x, number of iterations needed] as a 2-tuple. Or, if the solution did not converge. None.

LU = numpy.array([[0, 1/2, 1/3], [1/2, 0, 1/4], [1/3, 1/4, 0]], numpy.float64)
b = numpy.array([.1, .1, .1], numpy.float64)

def jacobi_iter(x0, tol, M):
    N = 0
    while N < M:
        prevX = x0
        x0 = matrix.powerMult(-LU, x0) + b
        diffVect = numpy.subtract(x0, prevX)
        N += 1
        if numpy.max(numpy.abs(diffVect)) <= tol:
            result = [x0, N]
            return result
    return None



