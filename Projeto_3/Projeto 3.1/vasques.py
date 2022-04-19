from sys import stdin, stdout


class Node:

    def __init__(self, x):

        self.categoria = x[0]
        self.valor = int(x[1])
        self.child = []


def newNode(array):
    temp = Node(array)
    return temp


def PrintTree(root):

    if (root == None):
        return

    q = []
    q.append(root)
    while (len(q) != 0):

        n = len(q)
        payload = ""
        while (n > 0):
            p = q[0]
            q.pop(0)
            payload += f"{p.categoria}({p.valor}) "

            for i in range(len(p.child)):
                q.append(p.child[i])
            n -= 1
        payload = payload.rstrip()
        outln(payload)


def backtracking(node):
    soma = 0
    q = node.child
    for i in q:
        soma += backtracking(i)
    soma += node.key
    node.valor = soma
    return soma


def readln():
    return stdin.readline().rstrip().split(" ")


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def populateTree(root, x):
    for i in range(int(x[2])):
        a = readln()
        (root.child).append(newNode(a)) 
        if(int(a[2]) != 0):
            populateTree(root.child[i], a)


if __name__ == '__main__':
    x = readln()
    root = newNode(x)
    populateTree(root, x)
    backtracking(root)
    PrintTree(root)