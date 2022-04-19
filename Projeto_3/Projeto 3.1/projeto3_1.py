from sys import stdin, stdout


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
        out_ln(string.rstrip())


def sum_values(node):
    soma = 0
    q = node.children
    for i in q:
        soma += sum_values(i)
    soma += node.value
    node.value = soma
    return soma


def insert_nodes(root, data):
    # First node already in the tree
    for i in range(int(data[2])):
        new_data = read_ln()
        n_children = int(new_data[2])
        root.children.append(Tree(new_data))

        # Keeps inserting on the left of the tree
        if n_children != 0:
            insert_nodes(root.children[i], new_data)


def main():
    first_node = read_ln()
    root = Tree(first_node)
    insert_nodes(root, first_node)
    sum_values(root)
    print_tree(root)


if __name__ == '__main__':
    main()