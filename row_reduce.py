__author__ = 'Orange Blossom'
import numpy as np

def l_reduce(l, c):
    b = np.copy(c)
    length = l.shape[0]
    for row in range(0, length - 1):
        for subrow in range (row + 1, length):
            b[subrow] -= b[row]*(l[subrow][row]/l[row][row])
            l[subrow][row] = 0
    for row in range(0, length):
        b[row] /= l[row][row]
        l[row][row] = 1
    return(b)

def r_reduce(l, c):
    b = np.copy(c)
    length = l.shape[0]
    for row in range(length - 1, 0, -1):
        for subrow in range (row - 1, - 1, -1):
            b[subrow] -= b[row]*(l[subrow][row]/l[row][row])
            l[subrow][row] = 0
    for row in range(0, length):
        b[row] /= l[row][row]
        l[row][row] = 1
    return(b)