import numpy as np
import matrixMultiplication as mm
import qr_fact_househ as qr
import row_reduce


def solve_qr_b(ab):
    length = ab.shape[1]
    a = np.array(ab[0:length - 1, 0:length -1])
    b = np.array(ab[0:length - 1, length -1: length])
    qrTuple = qr.qr_fact_househ(a)
    q = qrTuple[0]
    r = qrTuple[1]
    x = row_reduce.r_reduce(r, mm.matrix_vector_vertical_mult(q.T, b))
    errorVector = mm.matrix_vector_vertical_mult(a, x) - b
    error = np.max(np.abs(errorVector))
    return [x,error]