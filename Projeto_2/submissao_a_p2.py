from sys import stdin, stdout
import time
import random


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def main():
    n = [25000, 50000, 75000, 100000, 125000]

    for n_elements in n:
        array = [random.randint(0, 1000000) for i in range(n_elements)]
        aux = 0
        start = time.time()
        for i in range(int(n_elements)):
            for j in range(int(n_elements)):
                dif = abs(int(array[i]) - int(array[j]))
                if aux < dif:
                    aux = dif
        end = time.time()
        print("Time " + str(n_elements))
        print(end - start)
        print("------")
        #outln(aux)


if __name__ == "__main__":
    main()
