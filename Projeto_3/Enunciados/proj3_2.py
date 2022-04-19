# -*- coding: utf-8 -*-
from sys import stdin, stdout
import time


class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


class avlTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def find(self, num):
        return self._find(num, self.root)

    def _insert(self, data, root):
        # insert
        if (root is None):
            root = node(data)
        else:
            if (data.num < root.data.num):
                root.left = self._insert(data, root.left)
            else:
                root.right = self._insert(data, root.right)

        # balance tree
        eqFactor = self._getHeight(root.left) - self._getHeight(root.right)
        if (eqFactor < -1):
            if (data.num < root.right.data.num):
                # right left rotation
                root.right = self._rotRight(root.right)
                root = self._rotLeft(root)
            else:
                # left rotation
                root = self._rotLeft(root)
        elif (eqFactor > 1):
            if (data.num < root.left.data.num):
                # right rotation
                root = self._rotRight(root)
            else:
                # left right rotation
                root.left = self._rotLeft(root.left)
                root = self._rotRight(root)

        return root

    def _find(self, num, root):
        if (root is None):
            return None
        elif (num == root.data.num):
            return root.data
        elif (num < root.data.num):
            return self._find(num, root.left)
        else:
            return self._find(num, root.right)

    def _getHeight(self, root):
        if (root is None):
            return 0
        else:
            return max(self._getHeight(root.left), self._getHeight(root.right)) + 1

    def _rotRight(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        return newRoot

    def _rotLeft(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        return newRoot

    def _printOrder(self, node):
        if (node is None):
            out = ''
        else:
            out = self._printOrder(node.left) + '\n' + str(node) + '\n' + self._printOrder(node.right)
        return out.strip()

    def __str__(self):
        return self._printOrder(self.root)


class register:
    def __init__(self, num):
        self.num = num
        self.vacines = []

    def insertVacine(self, vacine):
        self.vacines.append(vacine)  # O(1)
        self.vacines.sort(key=lambda x: x.name)  # O(N log N)

    def findVacine(self, name):
        # O (N)
        for v in self.vacines:
            if v.name == name:
                return v
        return None

    def __str__(self):
        return str(self.num) + ' ' + ' '.join(str(v) for v in self.vacines)


class vacine:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return self.name + ' ' + self.date


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write('\n')


def main():
    tree = avlTree()
    insertTime = 0
    searchTime = 0

    command = readln()
    while (command != 'FIM'):
        command = command.split()
        op = command[0]
        if (op == 'ACRESCENTA'):
            t0 = time.process_time_ns()  # TIME START [INSERT]
            num = int(command[1])
            reg = tree.find(num)
            if (reg is None):
                # user not registered
                reg = register(num)
                vac = vacine(command[2], command[3])
                reg.insertVacine(vac)
                tree.insert(reg)
                insertTime += time.process_time_ns() - t0  # TIME STOP [INSERT]
                outln('NOVO UTENTE CRIADO')
            else:
                # user found
                vac = reg.findVacine(command[2])
                if (vac is None):
                    # vacine not found
                    vac = vacine(command[2], command[3])
                    reg.insertVacine(vac)
                    insertTime += time.process_time_ns() - t0  # TIME STOP [INSERT]
                    outln('NOVA VACINA INSERIDA')
                else:
                    # vacine found
                    vac.date = command[3]
                    insertTime += time.process_time_ns() - t0  # TIME STOP [INSERT]
                    outln('VACINA ATUALIZADA')
        elif (op == 'CONSULTA'):
            t0 = time.process_time_ns()  # TIME START [SEARCH]
            reg = tree.find(int(command[1]))
            searchTime += time.process_time_ns() - t0  # TIME STOP [SEARCH]
            if (reg is None):
                outln('NAO ENCONTRADO')
            else:
                outln(reg)
                outln('FIM')
        elif (op == 'LISTAGEM'):
            outln(tree)
            outln('FIM')
        elif (op == 'APAGA'):
            tree = avlTree()
            outln('LISTAGEM DE NOMES APAGADA')

        command = readln()

    outln('TIME: ' + str(insertTime + searchTime))


if (__name__ == '__main__'):
    main()
