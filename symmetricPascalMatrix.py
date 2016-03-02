_author_ = 'Albert'
import numpy as np
import matrixMultiplication as mm
import qr_fact_givens as qfg
import qr_fact_househ as qfh

def generate_pascal(size):
    pascalMatrix = np.zeros([size,size], float)
    pascalMatrix[0][0] = 1
    pascalMatrix[0][1] = 1
    pascalMatrix[1][0] = 1
    for row in range(2, size):
        pascalMatrix[row][0] = 1
        pascalMatrix[0][row] = 1
        for col in 	range(1, size - 1):
            pascalMatrix[row-col][col] = pascalMatrix[row-col][col-1] + pascalMatrix[row-col-1][col]

    for col in range(1, size):
        for increment in range(0, size - col):
            pascalMatrix[size - increment - 1][col + increment] = pascalMatrix[size -increment - 1][col + increment - 1] + pascalMatrix[size -increment - 2][col + increment]

    return pascalMatrix

def generate_pascal_b(size):
    b = np.zeros(size,float)[np.newaxis].T
    for row in range(0, size):
        b[row] = 1.0/(row + 1.0)
    return b

def lu_fact ( u ):
    v = np.copy(u)
    length = v.shape[0]
    l = np.identity(length, float)
    offset = 0
    for x in range(0, length):
        cont = 1
        if v[x - offset][x] == 0:
            cont = 0
            for y in range(x + 1 - offset, length - 1):
                if v[y][x] != 0:
                    interchange(v, x, y)
                    interchange(l, x, y)
                    cont = 1
                    break
        if not cont:
            offset += 1
        else:
            for y in range(x + 1 - offset, length):
                if v[y][x] != 0:
                    temp = v[y][x]
                    v[y] *= v[x - offset][x]
                    v[y] -= (v[x - offset]) * temp
                    v[y] /= v[x - offset][x]
                    l[y][x] += temp/v[x - offset][x]
    err = np.max(np.abs(u - mm.matrixMult(l,v)))
    return [l, v, err]

def interchange (a, row1, row2):
    temp = a[row1]
    a[row1] = a[row2]
    a[row2] = temp