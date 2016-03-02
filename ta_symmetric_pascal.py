__author__ = 'Orange Blossom'

import symmetricPascalMatrix
import solve_qr_b_givens
import solve_qr_b_househ
import solve_lu_b
import numpy as np


for n in range(2, 13):
    pascalMatrix = symmetricPascalMatrix.generate_pascal(n)
    b = symmetricPascalMatrix.generate_pascal_b(n)
    aug = np.concatenate([pascalMatrix, b], axis=1)
    householder = solve_qr_b_househ.solve_qr_b(aug)
    givens = solve_qr_b_givens.solve_qr_b(aug)
    lu = solve_lu_b.solve_lu_b(aug)
    print("\nFor a ", n, "x", n, " matrix:\n")
    print("\nHouseholder:\n",
          "Solution:\n",
          householder[0],
          "\nError:\n",
          householder[1],
          "\n\nGivens:\n",
          "\nSolution:\n",
          givens[0],
          "\nError:\n",
          givens[1],
          "\n\nLU:\n",
          "\nSolution:\n",
          lu[0],
          "\nError:\n",
          lu[1])