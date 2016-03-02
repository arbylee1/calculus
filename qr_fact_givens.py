# QR-factorization of nxn matrix that uses Givens Rotations
# Return matrices L and U, and the error ||QR-A||

import numpy as np
import math
import matrixMultiplication as mm;


def qr_fact_givens(b):
    a = np.copy(b)
    length = a.shape[0]
    q = np.identity(length, float)
    for piv in range(0, length - 1):
        for tar in range(piv + 1, length):
            index = np.identity(length, float)
            if a[tar, piv] != 0:
                x = a[piv, piv]
                y = a[tar, piv]
                cos = x / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
                sin = -y / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
                difference = abs(piv - tar)
                index[piv, piv] = cos
                index[piv, piv+difference] = -sin
                index[tar, piv] = sin
                index[tar, piv+difference] = cos
                q = mm.matrixMult(q, index.T)
                a = mm.matrixMult(index, a)
                a[tar, piv] = 0

    qr = mm.matrixMult(q,a)
    diff = np.subtract(qr, b)
    diff = np.absolute(diff)
    err = diff.max()
    return [q, a, err]
