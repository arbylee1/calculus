_author_ = 'Albert'

# QR-factorization of nxn matrix that uses Householder Rotations
# Return matrices L and U, and the error ||QR-A||

import numpy as np
import power_method as pm
import matrixMultiplication as mm
from numpy.linalg import inv


def qr_fact_househ(a):
    r = np.copy(a)
    length = r[0].size
    q = np.identity(length, float)
    for col in range(0, length - 1):
        v = np.zeros(length, float)
        for rows in range(col, length):
            v[rows] = r[rows][col]
        v[col] += np.dot(v,v)**0.5
        u = v/(np.dot(v,v)**0.5)
        h = np.subtract(np.identity(length, float), 2*mm.vectorMult(u, u.T))
        r = mm.matrixMult(h, r)
        for rows in range(col + 1, length):
            r[rows, col] = 0
        q = mm.matrixMult(q, h.T)
    qr = mm.matrixMult(q,r)
    difference = np.subtract(qr, a)
    return [q, r, np.max(np.abs(difference))]
