__author__ = 'Ecclesia'

import jacobi_iter as j
import gs_iter as gs
import numpy
import random

import csv
with open('Part 2 Iterations.csv', 'w') as p2file:
    writer = csv.writer(p2file, delimiter=',', lineterminator = '\n')

    # Analysis with 100 x0 guesses
    i = 0
    print("Start Jacobi")
    writer.writerow(['Jacobi x0', 'Iterations'])
    while i < 10:
        # Generate x_initial with random floating-point entries in range [-1,1]
        xRandom = numpy.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)], numpy.float64)
        writer.writerow(j.jacobi_iter(xRandom, .00005, 100))
        i += 1
    print("\n End Jacobi \n")

    j = 0
    print("Start Gauss-Seidel")
    writer.writerow(['Gauss-Seidel x0', 'Iterations'])
    while j < 10:
        # Generate x_initial with random floating-point entries in range [-1,1]
        yRandom = numpy.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)], numpy.float64)
        writer.writerow(gs.gs_iter(yRandom, .00005, 100))
        j += 1
    print("\n End Gauss-Seidel\n")







