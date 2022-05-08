from sys import stdin, stdout
import time
import random

def readln():
    return stdin.readline().rstrip().split(' ')


def outln(n):
    stdout.write(str(n))
    stdout.write('\n')


def dualPivotQuickSort(arr, low, high):
    if low < high:
        lp, rp = partition(arr, low, high)

        dualPivotQuickSort(arr, low, lp - 1)
        dualPivotQuickSort(arr, lp + 1, rp - 1)
        dualPivotQuickSort(arr, rp + 1, high)


def partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]

    while k <= g:

        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1

        else:
            while arr[g] > q and k < g:
                g -= 1

            arr[k], arr[g] = arr[g], arr[k]
            g -= 1

            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1

        k += 1

    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]

    return j, g

def percentil(array, num):
    count = 0
    for i in array:
        if i == num:
            break
        elif i < num:
            count += 1

    return int((count * 100) / len(array))


if __name__ == '__main__':
    if __name__ == '__main__':
        list = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
        for j in list:
            print("--- Valores pra %d ---" % j)
            raster = [random.randrange(0, 10000) for _ in range(j)]
            perc = [random.randrange(0, 10000) for _ in range(j)]
            tic = time.perf_counter()
            dualPivotQuickSort(raster, 0, len(raster) - 1)
            for i in range(j):
                percentil(raster, perc[i])
            toc = time.perf_counter()
            print(toc - tic)
            print('\n')
        ##readln()