__author__ = 'Orange Blossom'

import sys
import numpy as np
import solve_qr_b_givens
import solve_lu_b
import solve_qr_b_househ

np.set_printoptions(precision=6)
path = sys.argv[1]
arr = np.loadtxt(path, float)
print("Original Array: \n", arr)
print("\nQR Factorization (Householder)\n")
answer = solve_qr_b_househ.solve_qr_b(arr)
print("x:")
print(answer[0])
print("\nError:")
print(answer[1])
print("\nQR Factorization (Givens)\n")
answer = solve_qr_b_givens.solve_qr_b(arr)
print("x:")
print(answer[0])
print("\nError:")
print(answer[1])
print("\nLU Factorization\n")
answer = solve_lu_b.solve_lu_b(arr)
print("x:")
print(answer[0])
print("\nError:")
print(answer[1])