from sys import stdin, stdout
from time import time, perf_counter
import random

def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def cenas(n_elements):
    array = [random.randint(0, 1000000) for i in range(n_elements)]
    start = time()
    max = -1
    min = 1000001
    for i in array:
        if max < int(i):
            max = int(i)
        elif min > int(i):
            min = int(i)
    dif = max - min
    end = time()

    print("Time " + str(n_elements))
    print(end - start)


def main():
    perf_counter()
    cenas(25000)
    cenas(50000)
    cenas(75000)
    cenas(100000)
    cenas(125000)
    input()

    #outln(dif)


if __name__ == "__main__":
    main()
