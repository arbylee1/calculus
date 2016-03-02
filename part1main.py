__author__ = 'Orange Blossom'

import csv
import symmetricPascalMatrix
import numpy as np
import solve_lu_b
import solve_qr_b_givens
import solve_qr_b_househ

with open('Part 1 Errors.csv', 'w') as p2file:
    writer = csv.writer(p2file, delimiter=',', lineterminator = '\n')
    number = 13
    writer.writerow(["Size", "Householder", "Givens","LU"])
    for n in range(2, 13):
        pascalMatrix = symmetricPascalMatrix.generate_pascal(n)
        b = symmetricPascalMatrix.generate_pascal_b(n)
        aug = np.concatenate([pascalMatrix, b], axis=1)
        householder = solve_qr_b_househ.solve_qr_b(aug)
        givens = solve_qr_b_givens.solve_qr_b(aug)
        lu = solve_lu_b.solve_lu_b(aug)
        writer.writerow([n, householder[1], givens[1], lu[1]])