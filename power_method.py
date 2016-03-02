# power method to approximate en e'value and e'vecor for nxn
# inputs should take in A, initial guess v, tolerance, max num iterate before quitting, N
# outputs are e'value and e'vector, number of iterations -> if N times then return none

import numpy as np
import matrixMultiplication as mm
import math as math

def power_method(A, v, tol, N):
    u = np.copy(v)
    u = u.flatten()
    u =  u/np.max(np.abs(u))
    w = np.ones(v.shape[0])
    numIter = 0
    limiting = 0.0
    prevLimiting = 0
    total = 0
    while (numIter < N):
        prevU = u
        u = mm.powerMult(A, u)
        numerator = mm.vectorMultF(w, u)
        denominator = mm.vectorMultF(w, prevU)
        u /= np.max(np.abs(u))
        if numIter > 1:
            prevLimiting = limiting
        limiting = numerator / denominator
        check = abs(limiting - prevLimiting)
        if check <= tol:
            return (limiting, u, numIter)
        numIter += 1
    return None

def small_eigen(A):
    v = np.array([1,0])
    min = power_method(two_by_two_inverse(A), v, 0.00005, 100)
    return min

def big_eigen(A):
    v = np.array([1.0,0.0], float)
    max = power_method(A, v, 0.00005, 100)
    return max

def two_by_two_inverse(A):
    determinant_inverse = 1/determinant(A)
    temp = A[0][0]
    A[0][0] = A[1][1]
    A[1][1] = temp
    A[1][0] = -A[1][0]
    A[0][1] = -A[0][1]
    return A*determinant_inverse

def determinant(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    return a*d -b*c