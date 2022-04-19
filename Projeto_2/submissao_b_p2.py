from sys import stdin, stdout
import random, time


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def main():
    n_elements = 125000
    array = [random.randint(0, 1000000) for i in range(n_elements)]
    start = time.time()
    array.sort()
    dif = abs(int(array[-1]) - int(array[0]))
    end = time.time()
    print("Time " + str(n_elements))
    print(end - start)
    outln(dif)


if __name__ == "__main__":
    main()
