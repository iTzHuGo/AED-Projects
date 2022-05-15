from math import floor
from sys import stdin, stdout
from random import randrange
from time import time


def tempos():
    list = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

    for NUM in list:
        med = []
        file = open('tempos_4.3.txt', 'a')
        #file.write("--- Valores pra" + str(NUM) + "---\n")
        print("--- Valores pra %d ---" % NUM)
        #for i in range(10):
        raster = [randrange(0, 10000) for _ in range(NUM)]
        perc = [randrange(0, 10000) for _ in range(NUM)]
        tic = time()
        radix_sort(raster)
        percentil(raster, perc)
        toc = time()
        t = toc - tic
        med.append(t)
        # x = 0
        # for i in med:
        #     x += i
        # x /= 10

        file.write(str(t) + "\n")
        print("--- %f seg ---" % t)
        print()
        file.close()


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


def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radix_sort(array):
    maximum = -1
    for value in array:
        if value > maximum:
            maximum = value

    place = 1
    while maximum // place > 0:
        counting_sort(array, place)
        place *= 10


def percentil(matrix, input_array):
    # input_array = []
    results = []
    # for x in read_ln():
    #     input_array.append(int(x))
    aux = 0
    for i in range(len(input_array)):
        if input_array[i] <= matrix[i]:
            break
        aux = i + 1

    res = floor((aux / len(matrix)) * 100)
    results.append(res)
    aux = 0

    return results


def calculate_amplitude(matrix):
    amp = matrix[-1] - matrix[0]
    return amp


def calc_mediana(matrix):
    index = len(matrix) - 1
    if len(matrix) % 2 == 0:
        res = matrix[index // 2] + matrix[(index // 2) + 1]
        res //= 2
    else:
        res = matrix[index // 2]
    print(res)


def main():
    # m = []
    # op = read_ln()
    # while op[0] != "TCHAU":
    #
    #     if op[0] == "RASTER":
    #         m = read_matrix(op[1], op[2])
    #         m = count_sort(m)
    #         print(m)
    #     elif op[0] == "AMPLITUDE":
    #         amp = calculate_amplitude(m)
    #         print(amp)
    #
    #     elif op[0] == "PERCENTIL":
    #         percentil_values = percentil(m, int(op[1]))
    #         for i in range(len(percentil_values)):
    #             if i != len(percentil_values) - 1:
    #                 print(percentil_values[i], end=' ')
    #             else:
    #                 print(percentil_values[i])
    #
    #     elif op[0] == "MEDIANA":
    #         calc_mediana(m)
    #
    #     op = read_ln()
    tempos()


if __name__ == "__main__":
    main()
