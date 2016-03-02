__author__ = 'Jacobi Bryant, Not Amy'

import numpy as np
import sys
import jacobi_iter

np.set_printoptions(precision=6)
path = sys.argv[1]
tolerance = sys.argv[2]
iterations = sys.argv[3]
x0 = np.loadtxt(path, float)[np.newaxis].T
jacobi = jacobi_iter.jacobi_iter(x0, float(tolerance), int(iterations))
print("Jacobi Iteration\n")
if jacobi is None:
    print("The solution could not be estimated within ",
          iterations, "iterations.")
else:
    print("Approximate solution:\n",
        jacobi[0][np.newaxis].T, "\nIterations:\n",
        jacobi[1])