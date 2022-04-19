from sys import stdin, stdout


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            outln(matrix[i][j])
            if j != len(matrix[i]) - 1:
                outln(' ')

        stdout.write('\n')


def rotate90(box):
    rows = len(box)
    cols = len(box[0])

    box2 = [[""] * rows for _ in range(cols)]

    for x in range(rows):
        for y in range(cols):
            box2[y][rows - x - 1] = box[x][y]
    return box2


def main():
    lines, columns = readln().split(' ')
    matrix = []

    for line in range(int(lines)):
        aux = readln().split(' ')
        matrix.append(aux)

    matrix90 = rotate90(matrix)
    outln('90\n')
    print_matrix(matrix90)
    matrix180 = rotate90(matrix90)
    outln('180\n')
    print_matrix(matrix180)
    matrix270 = rotate90(matrix180)
    outln('270\n')
    print_matrix(matrix270)


if __name__ == '__main__':
    main()
