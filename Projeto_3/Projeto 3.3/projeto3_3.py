from sys import stdin, stdout


def read_ln():
    return stdin.readline().rstrip().split(" ")


def out_ln(n):
    stdout.write(str(n))
    stdout.write("\n")


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.print(self.root, 0)

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def find(self, user):
        return self._find(user, self.root)

    def _insert(self, data, root):
        if root is None:
            root = Node(data)
        elif data.user < root.data.user:
            root.left = self._insert(data, root.left)
        else:
            root.right = self._insert(data, root.right)

        balance = self.get_height(root.left) - self.get_height(root.right)
        if balance < -1:
            if data.user < root.right.data.user:
                # right left
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
            else:
                # left
                root = self.rotate_left(root)
        elif balance > 1:
            if data.user < root.left.data.user:
                # right
                root = self.rotate_right(root)
            else:
                # left right
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)

        return root

    def _find(self, user, root):
        if root is None:
            return None
        elif user == root.data.user:
            return root.data
        elif user < root.data.user:
            return self._find(user, root.left)
        else:
            return self._find(user, root.right)

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def print(self, node, n):
        if node is None:
            string = ''
        else:
            if n == 0:
                if node.left is None:
                    string = '\n' + str(node.data.user) + ' ' + str(node) + '\n' + \
                             str(self.print(node.right, 1))

                elif node.right is None:
                    string = '\n' + str(self.print(node.left, 1)) + '\n' + str(node.data.user) + ' ' + str(node)

                else:
                    string = '\n' + str(self.print(node.left, 1)) + '\n' + str(node.data.user) + ' ' + str(node) + '\n'\
                             + str(self.print(node.right, 1)) + '\n'
            else:
                if node.right is None:
                    string = '\n' + str(node.data.user) + ' ' + str(node) + '\n' + str(self.print(node.left, 1)) + '\n'

                elif node.left is None:
                    string = '\n' + str(node.data.user) + ' ' + str(node) + '\n' + str(self.print(node.left, 1)) + '\n'

                else:
                    string = '\n' + str(self.print(node.left, 1)) + '\n' + str(node.data.user) + ' ' + str(node) + '\n'\
                             + str(self.print(node.right, 1)) + '\n'

        return string


class Register:
    def __init__(self, user):
        self.user = user
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        self.cards.sort(key=lambda x: x.num)

    def find_card(self, num):
        for c in self.cards:
            if c.num == num:
                return c
        return None

    def print(self):
        aux = ""
        length = len(self.cards)
        count = 0
        for c in self.cards:
            count += 1
            if count == length:
                aux += str(c)
            else:
                aux += str(c) + ' '

        return aux

    def __str__(self):
        return self.print()


class Card:
    def __init__(self, num, exp):
        self.num = num
        self.exp = exp

    def __str__(self):
        return self.num + ' ' + self.exp


def inputs():
    root = AVLTree()
    line = read_ln()
    file = open("teste.txt", 'a')
    while line[0] != "FIM":
        op = line[0]
        if op == "ACRESCENTA":
            #      0         1                     2                       3
            # ACRESCENTA <username> <número de cartão de crédito> <data de expiração>
            user = line[1]
            usr = root.find(user)
            if usr is None:
                # user is not registered
                usr = Register(user)
                card = Card(line[2], line[3])
                usr.add_card(card)
                root.insert(usr)
                #out_ln("NOVO UTILIZADOR CRIADO")
                file.write("NOVO UTILIZADOR CRIADO\n")
            else:
                # user is registered
                card = usr.find_card(line[2])
                if card is None:
                    # card does not exist
                    card = Card(line[2], line[3])
                    usr.add_card(card)
                    #out_ln("NOVO CARTAO INSERIDO")
                    file.write("NOVO CARTAO INSERIDO\n")
                else:
                    # card exists
                    card.exp = line[3]
                    #out_ln("CARTAO ATUALIZADO")
                    file.write("CARTAO ATUALIZADO\n")

        elif op == "CONSULTA":
            #     0        1
            # CONSULTA <username>
            usr = root.find(line[1])
            if usr is None:
                # user is not registered
                #out_ln("NAO REGISTADO")
                file.write("NAO REGISTADO\n")
            else:
                for card in usr.cards:
                    #out_ln(card)
                    file.write(card.__str__() + "\n")
                #out_ln("FIM")
                file.write("FIM\n")

        elif op == "LISTAGEM":
            for line in root.__str__().split('\n'):
                if line.strip() != '':
                    #out_ln(line)
                    file.write(line + '\n')
            #out_ln("FIM")
            file.write("FIM\n")

        elif op == "APAGA":
            root = AVLTree()
            #out_ln("LISTAGEM APAGADA")
            file.write("LISTAGEM APAGADA\n")

        line = read_ln()


if __name__ == '__main__':
    inputs()
