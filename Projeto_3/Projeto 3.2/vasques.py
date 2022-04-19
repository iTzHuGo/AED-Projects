import sys
# https://www.codesdope.com/course/data-structures-splay-trees/


def readln():
    return sys.stdin.readline().rstrip().split(" ")


def outln(n):
    sys.stdout.write(str(n))
    sys.stdout.write("\n")


class Node:
    def __init__(self, data):
        self.nome = data[1]
        self.hash = data[2]
        self.oferta = int(data[3])
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent != None:
            if n.parent == self.root:
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:
                p = n.parent
                g = p.parent

                if n.parent.left == n and p.parent.left == p:
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif n.parent.right == n and p.parent.right == p:
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if(n.nome == y.nome):
                outln("ARTIGO JA EXISTENTE")
                return None
            elif n.nome < temp.nome:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None:
            self.root = n
        elif n.nome < y.nome:
            y.left = n
        else:
            y.right = n

        self.splay(n)
        outln("NOVO ARTIGO INSERIDO")

    def oferta(self, n, x, oferta):
        if(n == None):
            return "ARTIGO NAO REGISTADO"
        if x == n.nome:
            self.splay(n)
            n.oferta = oferta
            return "OFERTA ATUALIZADA"

        elif x < n.nome:
            return self.oferta(n.left, x, oferta)
        elif x > n.nome:
            return self.oferta(n.right, x, oferta)
        else:
            return "ARTIGO NAO REGISTADO"

    def consulta(self, n, x):
        if(n == None):
            return "ARTIGO NAO REGISTADO"
        if x == n.nome:
            self.splay(n)
            payload = n.nome+" "+n.hash+" "+str(n.oferta)
            outln(payload)
            return "FIM"

        elif x < n.nome:
            return self.consulta(n.left, x)
        elif x > n.nome:
            return self.consulta(n.right, x)
        else:
            return "ARTIGO NAO REGISTADO"

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            outln(n.nome)
            self.inorder(n.right)


def EsquerdaDireita(root: SplayTree) -> None:
    if (not root):
        return

    if root.left:
        EsquerdaDireita(root.left)
    payload = root.nome+" "+root.hash+" "+str(root.oferta)
    outln(payload)
    if root.right:
        EsquerdaDireita(root.right)


def deleteTree(node):
    if node != None:
        deleteTree(node.left)
        deleteTree(node.right)
        del node


# Add -> t.insert(Node(x))
# Oferta ->print(t.oferta(t.root, "Pintura1", 150))
# Consulta -> print(t.consulta(t.root, "Pintura1"))
# EsquerdaDireita -> EsquerdaDireita(t.root)
if __name__ == '__main__':
    t = SplayTree()

    while(True):
        a = readln()
        if(a[0] == "ARTIGO"):
            t.insert(Node(a))
        elif(a[0] == "OFERTA"):
            outln(t.oferta(t.root, a[1], int(a[2])))
        elif(a[0] == "CONSULTA"):
            outln(t.consulta(t.root, a[1]))
        elif(a[0] == "LISTAGEM"):
            EsquerdaDireita(t.root)
            outln("FIM")
        elif(a[0] == "APAGA"):
            deleteTree(t.root)
            t.root = None
            outln("CATALOGO APAGADO")
        elif(a[0] == "FIM"):
            break
