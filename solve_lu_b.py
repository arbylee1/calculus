_author_ = 'Albert'

import numpy as np
import matrixMultiplication as mm
import symmetricPascalMatrix as lu
import row_reduce


def solve_lu_b(ab):
    length = ab.shape[1]
    a = np.array(ab[0:length - 1, 0:length -1])
    b = np.array(ab[0:length - 1, length -1: length])
    luTuple = lu.lu_fact(a)
    l = luTuple[0]
    u = luTuple[1]
    c = row_reduce.l_reduce(l,b)
    x = row_reduce.r_reduce(u,c)
    ax = mm.matrix_vector_vertical_mult(a,x)
    errorVector = np.subtract(ax,b)
    error = np.max(np.abs(errorVector))
    return[x,error]