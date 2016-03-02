_author_ = 'Amy'

import numpy as np

def matrixMult(matrixA, matrixB):
    length = len(matrixA[:, 1])
    value = 0.0
    # result = np.empty(length, dtype = np.float)
    result = np.zeros(shape=(length,length))
    for row in range(0, length):
        #column for new Matrix
        for col in range(0, length):
            for i in range(0, length):
                value += matrixA[row, i] * matrixB[i, col]
            result[row][col] = value
            value = 0.0
    return result

def vectorMult(vRow, vCol):
    length = len(vRow)
    value = 0.0
    result = np.zeros(shape=(length,length))
    for row in range(0, length):
        for col in range(0, length):
            value = vRow[row] * vCol[col]
            result[row][col] = value
        value = 0.0
    return result

def powerMult(matrix, v):
    length = len(v)
    value = 0.0
    result = np.zeros(length)
    for row in range(0, length):
        for col in range(0, length):
            value += matrix[row][col] * v[col]
            result[row] = value
        value = 0.0
    return result

def vectorMultF(w, v):
    length = len(w)
    value = 0.0
    result = [0] * length
    for element in range(0, length):
        value += w[element] * v[element]
    return value

def matrix_vector_vertical_mult(matrix, v):
    length = matrix.shape[0]
    value = 0.0
    result = np.zeros(length)[np.newaxis].T
    for row in range (0, length):
        for col in range(0, length):
            value += matrix[row][col]*v[col]
        result[row] = value
        value = 0.0
    return result