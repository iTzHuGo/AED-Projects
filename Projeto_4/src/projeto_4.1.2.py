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


def insertion_sort(array):
    for i in range(1, len(array)):
        aux = array[i]
        j = i - 1
        while j >= 0 and aux < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = aux


def get_pivot(low, middle, high):
    if low <= middle <= high or high <= middle <= low:
        return middle
    if low <= high <= middle or middle <= high <= low:
        return high
    if middle <= low <= high or high <= low <= middle:
        return low


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high):
    if len(array) == 1:
        return array

    if high - low < 30:
        insertion_sort(array)

    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def percentil(matrix, n):
    input_array = []
    results = []
    for x in read_ln():
        input_array.append(int(x))
    aux = 0
    for i in input_array:
        for j in range(len(matrix)):
            if i <= matrix[j]:
                break
            aux = j + 1

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
    m = []
    op = read_ln()
    while op[0] != "TCHAU":

        if op[0] == "RASTER":
            m = read_matrix(op[1], op[2])
            quick_sort(m, 0, len(m) - 1)

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
