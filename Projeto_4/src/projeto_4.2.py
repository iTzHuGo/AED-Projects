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


def insertion_sort(array, start, end):
    for i in range(start, end + 1):
        cur = array[i]
        k = i

        while k - 1 >= start and array[k - 1] > cur:
            array[k] = array[k - 1]
            k -= 1

        array[k] = cur


def quick_sort(array, start, end, cutoff):
    # base
    if end - start < cutoff:
        insertion_sort(array, start, end)
        return

    pivot = array[end]

    # partition array
    i = start
    j = end - 1

    while i < j:
        i += 1
        j -= 1

        while array[i] < pivot:
            i += 1
        while pivot < array[j]:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    # swap pivot with i (when i > j => array[i] > pivot)
    array[i], array[end - 1] = array[end - 1], array[i]

    # recursive call
    quick_sort(array, start, i - 1, cutoff)
    quick_sort(array, i + 1, end, cutoff)


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
            quick_sort(m, 0, len(m) - 1, 30)

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
