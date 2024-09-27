import time
import tracemalloc


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.output_index = 0


class AVLTree():
    def __init__(self, Nodes, index=1):
        self.root = self.create_tree(Nodes, index)


    def create_tree(self, Nodes, index):
        if len(Nodes) == 1:
            return
        if index == 0:
            return

        root = Node(Nodes[index][0])
        root.left = self.create_tree(Nodes, Nodes[index][1])
        root.right = self.create_tree(Nodes, Nodes[index][2])
        self.fix_height(root)
        return root


    def height(self, node):
        if node is None:
            return 0
        return node.height


    def fix_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))


    def rotate_left(self, node):
        p = node.right
        node.right = p.left
        p.left = node
        return p


    def rotate_right(self, node):
        q = node.left
        node.left = q.right
        q.right = node
        return q


    def big_left_rotate(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)


    def get_balance(self, node):
        return self.height(node.right) - self.height(node.left)


    def print_tree(self):
        def tree_queue(root):
            if root is None:
                return
            nonlocal index
            root.output_index = index
            index += 1
            tree_queue(root.left)
            tree_queue(root.right)


        def print_tree_queue(root):
            if root is None:
                return
            nonlocal Nodes
            Nodes.append(map(str, (root.key,
            root.left.output_index if not root.left is None else '0',
            root.right.output_index if not root.right is None else '0')))
            print_tree_queue(root.left)
            print_tree_queue(root.right)

        index = 1
        Nodes = []
        tree_queue(self.root)
        print_tree_queue(self.root)
        return Nodes


def main():
    with open("input.txt") as f:
        n = int(f.readline())
        Nodes = [None] + [tuple(map(int, node.split())) for node in f.readlines()]


    tree = AVLTree(Nodes)

    if tree.get_balance(tree.root.right) == -1: #финальный поворот
        tree.root = tree.big_left_rotate(tree.root)
    else:
        tree.root = tree.rotate_left(tree.root)


    with open("output.txt", "w") as f:
        f.write(str(n) + '\n')
        for node in tree.print_tree():
            f.write(' '.join(node) + '\n')


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
