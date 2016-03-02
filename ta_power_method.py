__author__ = 'Orange Blossom'

import numpy as np
import sys
import power_method

np.set_printoptions(precision=6)
path = sys.argv[1]
tolerance = sys.argv[2]
iterations = sys.argv[3]
ab = np.loadtxt(path, float)
length = ab.shape[1]
a = np.array(ab[0:length - 1, 0:length -1])
b = np.array(ab[0:length - 1, length -1: length])
print(a)
print(b)
power = power_method.power_method(a, b, float(tolerance), int(iterations))
print("Power Method Approximation:\n")
if power is None:
    print("The eigenvalue did not converge within ",
          iterations, "iterations.")
else:
    print("Approximate eigenvalue:\n",
        power[0][np.newaxis].T, "\nApproximate eigenvector:\n",
        power[1])