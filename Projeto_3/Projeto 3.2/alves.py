from sys import stdin
from math import ceil
import string
import random
import time


class Node:
    def __init__(self, name, hashcode, val):
        self.name = name
        self.hashcode = hashcode
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return self.name + ' ' + self.hashcode + ' ' + str(self.val)


class SplayTree:
    def __init__(self):
        self.root = None

    def zag(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return

    def zig(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        return

    def splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.left:
                    # zig rotation
                    self.zig(x.parent)
                else:
                    # zag rotation
                    self.zag(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.zig(x.parent.parent)
                self.zig(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.zag(x.parent.parent)
                self.zag(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.zag(x.parent)
                self.zig(x.parent)
            else:
                # zag-zig rotation
                self.zig(x.parent)
                self.zag(x.parent)
        return

    def search(self, name, node):
        if node is None:
            return None

        elif name == node.name:
            self.splay(node)
            return node

        elif name < node.name:
            if node.left is not None:
                return self.search(name, node.left)

        elif name > node.name:
            if node.right is not None:
                return self.search(name, node.right)

        else:
            return None

    def insert(self, name, hashcode, value):
        node = Node(name, hashcode, value)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.name < x.name:
                x = x.left
            elif node.name == x.name:
                # print("ARTIGO JA EXISTENTE")
                return
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.name < y.name:
            y.left = node
        else:
            y.right = node
        # print("NOVO ARTIGO INSERIDO")
        self.splay(node)
        return

    def in_order(self, node):
        if node is None:
            return

        self.in_order(node.left)

        print(node)

        self.in_order(node.right)

    def delete_tree(self):
        self.root = None
        return


def readln():
    return stdin.readline().rstrip()


def menu():
    option = None
    tree = SplayTree()

    while option != "FIM":
        l = readln().split()
        option = l[0]
        if option == "ARTIGO":
            tree.insert(l[1], str(l[2]), int(l[3]))
        elif option == "OFERTA":
            y = tree.search(l[1], tree.root)
            if y is not None:
                y.val = l[2]
                print("OFERTA ATUALIZADA")
            else:
                print("ARTIGO NAO REGISTADO")
        elif option == "CONSULTA":
            y = tree.search(l[1], tree.root)
            if y is not None:
                print(f"{y.name} {y.hashcode} {y.val}")
                print("FIM")
            else:
                print("ARTIGO NAO REGISTADO")
        elif option == "LISTAGEM":
            tree.in_order(tree.root)
            print("FIM")
        elif option == "APAGA":
            tree.delete_tree()
            print("CATALOGO APAGADO")


# menu()


def cenario(no_consultas, option):
    letters = string.ascii_letters
    numbers = string.digits
    tree = SplayTree()
    timed = 0

    insercoes = []

    no_insercoes = 100

    # gerar inputs aleatorios
    for i in range(no_insercoes):
        name = ''.join(random.choice(letters) for i in range(12))
        hashcode = ''.join(random.choice(letters) for i in range(6))
        offer = ''.join(random.choice(numbers) for i in range(4))
        insercoes.append([name, hashcode, offer])

    for j in insercoes:
        tree.insert(j[0], j[1], int(j[2]))

    lim = ceil(0.05*len(insercoes))
    acessos_frequentes = insercoes[0:lim]
    acessos_nao_frequentes = insercoes[lim:]

    for i in range(no_consultas):
        a = random.randint(1, 10)
        if option == 1:
            if a <= 9:
                finding = random.choice(acessos_frequentes)
                # consulta um dos 5%
                start = time.perf_counter()
                tree.search(finding[0], tree.root)
                end = time.perf_counter()

            else:
                # consulta um dos restantes
                finding = random.choice(acessos_nao_frequentes)
                start = time.perf_counter()
                tree.search(finding[0], tree.root)
                end = time.perf_counter()

        else:
            finding = random.choice(insercoes)
            start = time.perf_counter()
            tree.search(finding[0], tree.root)
            end = time.perf_counter()
        timed += (end - start)

    return timed


def main_2():
    # numero de arvores
    trees = 10

    # numero de consultas
    n = [(25000 * i) for i in range(0, 41)]

    tempos_1 = []
    tempos_2 = []

    mean_1 = 0
    mean_2 = 0

    for no_consultas in n:

        print(no_consultas)

        for i in range(trees):
            mean_1 += cenario(no_consultas, 1)
            mean_2 += cenario(no_consultas, 2)

        mean_1 /= trees
        mean_2 /= trees

        tempos_1.append(mean_1)
        tempos_2.append(mean_2)

    print("Tempos_1")
    for i in tempos_1:
        a = str(i)
        print(a.replace('.', ','))

    print("Tempos_2")
    for i in tempos_2:
        a = str(i)
        print(a.replace('.', ','))

    return


main_2()
