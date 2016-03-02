__author__ = 'Orange Blossom'

import sys
import numpy as np
import qr_fact_househ
import qr_fact_givens
import symmetricPascalMatrix

np.set_printoptions(precision=6)
path = sys.argv[1]
arr = np.loadtxt(path, float)
print("Original Array: \n", arr)
print("\nQR Factorization (Householder)\n")
qrTuple = qr_fact_househ.qr_fact_househ(arr)
print("Q:")
print(qrTuple[0])
print("\nR:")
print(qrTuple[1])
print("\nError:")
print(qrTuple[2])
print("\nQR Factorization (Givens)\n")
qrTuple = qr_fact_givens.qr_fact_givens(arr)
print("Q:")
print(qrTuple[0])
print("\nR:")
print(qrTuple[1])
print("\nError:")
print(qrTuple[2])
print("\nLU Factorization\n")
qrTuple = symmetricPascalMatrix.lu_fact(arr)
print("L:")
print(qrTuple[0])
print("\nU:")
print(qrTuple[1])
print("\nError:")
print(qrTuple[2])