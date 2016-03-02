import numpy as np
import sys
import gs_iter

np.set_printoptions(precision=6)
path = sys.argv[1]
tolerance = sys.argv[2]
iterations = sys.argv[3]
x0 = np.loadtxt(path, float)[np.newaxis].T
gauss = gs_iter.gs_iter(x0, float(tolerance), int(iterations))
print("Gauss-Seidel Iteration\n")
if gauss is None:
    print("The solution could not be estimated within ",
          iterations, "iterations.")
else:
    print("Approximate solution:\n",
        gauss[0][np.newaxis].T, "\nIterations:\n",
        gauss[1])