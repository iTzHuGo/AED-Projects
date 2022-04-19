import string
from asyncio.windows_events import NULL
import random
from sys import stdin, stdout
from time import time


def read_ln():
    return stdin.readline().rstrip().split(" ")


def out_ln(n):
    stdout.write(str(n))
    stdout.write("\n")


class Tree:
    def __init__(self, data):
        self.category = data[0]
        self.value = int(data[1])
        self.children = []


def print_tree(root):
    if root is None:
        return

    queue = [root]
    while len(queue) != 0:
        n = len(queue)
        string = ''

        while n > 0:
            p = queue[0]
            queue.pop(0)
            string += f"{p.category}({p.value}) "

            for i in range(len(p.children)):
                queue.append(p.children[i])
            n -= 1
        #out_ln(string.rstrip())


def sum_values(node):
    soma = 0
    q = node.children
    for i in q:
        soma += sum_values(i)
    soma += node.value
    node.value = soma
    return soma


def insert_nodes(root, data, array):
    # First node already in the tree
    for i in range(int(data[2])):
        array.pop(0)
        new_data = array[0]
        n_children = int(new_data[2])
        root.children.append(Tree(new_data))

        # Keeps inserting on the left of the tree
        if n_children != 0:
            insert_nodes(root.children[i], new_data, array)


def gerarGlobalArray(disponiveis):
    array_global = []
    aux = disponiveis
    for i in range(aux+1):
        array, disponiveis = gerarUmArray(disponiveis)
        array_global.append(array)
    return array_global


def gerarUmArray(disponiveis):
    letras = string.ascii_lowercase
    array = [NULL] * 3
    array[0] = ""
    for i in range(10):
        array[0] += random.choice(letras)
    array[1] = random.randint(0, 5000)
    if disponiveis == 0:
        array[2] = 0
        return array, 0
    else:
        array[2] = random.randint(1, disponiveis)
    disponiveis -= array[2]
    return array, disponiveis


def main():
    #first_node = read_ln()
    tempos = [25000, 50000, 75000, 100000, 125000]
    durac = []
    for i in tempos:
        array = gerarGlobalArray(i)
        start = time()
        first_node = array[0]
        root = Tree(first_node)
        insert_nodes(root, first_node, array)
        sum_values(root)
        print_tree(root)
        end = time() - start
        durac.append(end)

    for i in durac:
        print(i)


if __name__ == '__main__':
    main()
