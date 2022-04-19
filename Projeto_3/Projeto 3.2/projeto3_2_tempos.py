from sys import stdin, stdout
from time import time


def read_ln():
    return stdin.readline().rstrip().split(" ")


def out_ln(n):
    stdout.write(str(n))
    stdout.write("\n")


class Node:
    def __init__(self, name, hash_code, value):
        self.left = None
        self.right = None
        self.parent = None
        self.name = name
        self.value = value
        self.hash_code = hash_code

    def __str__(self):
        return self.name + ' ' + self.hash_code + ' ' + str(self.value)


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data[1], data[2], data[3])
        new_node = None
        root = self.root

        while root is not None:
            new_node = root
            if node.name < root.name:
                root = root.left
            elif node.name == root.name:
                #out_ln("ARTIGO JA EXISTENTE")
                return
            else:
                root = root.right
        node.parent = new_node
        if new_node is None:
            self.root = node
        elif node.name < new_node.name:
            new_node.left = node
        else:
            new_node.right = node
        #out_ln("NOVO ARTIGO INSERIDO")
        self.splay(node)

    def search(self, node, name):
        if node is None:
            return

        elif name < node.name:
            if node.left is not None:
                return self.search(node.left, name)

        elif name > node.name:
            if node.right is not None:
                self.search(node.right, name)

        else:
            self.splay(node)
            return node

    def splay(self, node):
        while node.parent is not None:
            if node.parent.parent is None:
                if node == node.parent.left:
                    # zig rotation
                    self.rotate_right(node.parent)
                else:
                    # zag rotation
                    self.rotate_left(node.parent)
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                # zig-zig
                self.rotate_right(node.parent.parent)
                self.rotate_right(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                # zag-zag
                self.rotate_left(node.parent.parent)
                self.rotate_left(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.left:
                # zig-zag
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)
            else:
                # zag-zig
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)

    # zig
    def rotate_right(self, node):
        new = node.left
        node.left = new.right
        if new.right is not None:
            new.right.parent = node

        new.parent = node.parent
        if node.parent is None:
            self.root = new
        elif node == node.parent.right:
            node.parent.right = new
        else:
            node.parent.left = new

        new.right = node
        node.parent = new

    # zag
    def rotate_left(self, node):
        new = node.right
        node.right = new.left
        if new.left is not None:
            new.left.parent = node

        new.parent = node.parent
        if node.parent is None:
            self.root = new
        elif node == node.parent.left:
            node.parent.left = new
        else:
            node.parent.right = new

        new.left = node
        node.parent = new

    def print_listagem(self, node):
        if node is None:
            return
        self.print_listagem(node.left)
        # out_ln(node)
        self.print_listagem(node.right)

    def __str__(self):
        return self.print_listagem(self.root)


def inputs():
    s_tree = SplayTree()
    #line = read_ln()
    files = ["teste_c1_25000.txt", "teste_c1_50000.txt", "teste_c1_75000.txt", "teste_c1_100000.txt",
             "teste_c1_125000.txt"]
    for _ in range(5):
        for name in files:
            file = open(name, 'r')
            line = file.readline().split()
            start = time()
            while line[0] != "FIM":
                op = line[0]
                if op == "ARTIGO":
                    #   0      1      2              3
                    # ARTIGO <nome> <hash> <valor da oferta atual>
                    s_tree.insert(line)

                elif op == "OFERTA":
                    #    0      1            2
                    # OFERTA <nome> <valor da oferta atual>
                    nome = line[1]
                    node = s_tree.search(s_tree.root, nome)
                    if node is not None:
                        node.value = line[2]
                        #out_ln("OFERTA ATUALIZADA")
                    else:
                        pass
                        #out_ln("ARTIGO NAO REGISTADO")

                elif op == "CONSULTA":
                    #     0      1
                    # CONSULTA <nome>
                    artigo = s_tree.search(s_tree.root, line[1])
                    if artigo is None:
                        # artigo is not registered
                        #out_ln("ARTIGO NAO REGISTADO")
                        pass
                    else:
                        string = artigo.name + ' ' + artigo.hash_code + ' ' + artigo.value
                        #out_ln(string)
                        #out_ln("FIM")

                elif op == "LISTAGEM":
                    s_tree.print_listagem(s_tree.root)
                    #out_ln("FIM")

                elif op == "APAGA":
                    s_tree.root = None
                    #out_ln("CATALOGO APAGADO")

                line = file.readline().split()
            end = time() - start
            file.close()
            print(end)
            res = open("resultados.txt", 'a')
            res.write(str(end) + '\n')
            res.close()
        res = open("resultados.txt", 'a')
        res.write('\n')
        res.close()



if __name__ == '__main__':
    inputs()
