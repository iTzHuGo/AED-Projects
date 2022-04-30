from math import floor
from sys import stdin, stdout


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


def percentil(matrix, n):
    input_array = []
    results = []
    for x in read_ln():
        input_array.append(int(x))
    aux = 0
    for i in input_array:
        for j in matrix:
            if i > j:
                aux += 1
        res = floor((aux / len(matrix)) * 100)
        results.append(res)
        aux = 0
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


if __name__ == "__main__":
    main()
