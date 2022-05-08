from random import randrange
from time import time
from math import floor
from sys import stdin, stdout


def tempos():
    list = [25000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    for NUM in list:
        file = open('tempos_4.1.txt', 'a')
        file.write("--- Valores pra" + str(NUM) + "---")
        print("--- Valores pra %d ---" % NUM)
        for f in range(3):
            raster = [randrange(0, 10000) for _ in range(NUM)]
            perc = [randrange(0, 10000) for _ in range(NUM)]
            tic = time()
            for i in range(NUM):
                percentil(raster, perc)
            toc = time()
            t = toc - tic
            file.write("---" + str(t) + "seg ---")
            print("--- %f seg ---" % (toc - tic))
        print()


def read_ln():
    return stdin.readline().rstrip().split()


def out_ln(n):
    stdout.write(str(n))
    stdout.write("\n")


def read_matrix(lines, columns):
    matrix = []

    for line in range(int(lines)):
        aux = read_ln()
        for column in range(int(columns)):
            matrix.append(int(aux[column]))

    out_ln("RASTER GUARDADO")
    return matrix


def calculate_amplitude(matrix):
    maximum = -1
    minimum = 10001

    for value in matrix:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    amp = maximum - minimum
    return amp


def percentil(matrix, arr):
    # input_array = []
    results = []
    # for x in read_ln():
    #     input_array.append(int(x))
    aux = 0
    for i in arr:
        for j in matrix:
            if i > j:
                aux += 1
        res = floor((aux / len(matrix)) * 100)
        results.append(res)
        aux = 0
    print('Done')
    return results


# quicksort a ir por metade dos caminhos
# usar a mediana entre o primeiro o do meio e o do fim como pivot
def calc_mediana(matrix):
    index = len(matrix) - 1
    matrix.sort()
    if len(matrix) % 2 == 0:
        res = matrix[index//2] + matrix[(index//2) + 1]
        res //= 2
    else:
        res = matrix[index//2]
    print(res)


def main():
    """
    m = []
    op = read_ln()
    while op[0] != "TCHAU":
        if op[0] == "RASTER":
            m = read_matrix(op[1], op[2])

        elif op[0] == "AMPLITUDE":
            amp = calculate_amplitude(m)
            print(amp)

        elif op[0] == "PERCENTIL":
            percentil_values = percentil(m, int(op[1]))
            for i in range(len(percentil_values)):
                if i != len(percentil_values) - 1:
                    print(percentil_values[i], end=' ')
                else:
                    print(percentil_values[i])

        elif op[0] == "MEDIANA":
            calc_mediana(m)

        op = read_ln()
    """
    tempos()



if __name__ == "__main__":
    main()
