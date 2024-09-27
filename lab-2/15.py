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
    def __init__(self, n, Nodes, index=1):
        self.root = self.create_tree(Nodes, index)
        self.number_of_nodes = n


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

# ============================

    def height(self, node):
        if node is None:
            return 0
        return node.height


    def fix_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

#============================

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

#============================

    def get_balance(self, node):
        return self.height(node.right) - self.height(node.left)


    def balance_node(self, node):
        if self.get_balance(node) == 2:
            if self.get_balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if self.get_balance(node) == -2:
            if self.get_balance(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node

#============================

    def delete(self, root, key, is_delete_key=True):
        if is_delete_key:
            self.number_of_nodes -= 1

        if root is None:
            return root
        if key == root.key:
            if not (root.left or root.right): #если лист
                root = None
                return None

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            elif root.left is None:
                temp = root.right
                root = None
                return temp

            else:
                left_tree = root.left
                while left_tree.right is not None:
                    left_tree = left_tree.right
                root.key = left_tree.key

                root.left = self.delete(root.left, left_tree.key, False)

        else:
            if key < root.key:
                root.left = self.delete(root.left, key, False)
            elif key > root.key:
                root.right = self.delete(root.right, key, False)

        self.fix_height(root)
        balance = self.get_balance(root)
        if balance not in [-1, 0, 1]:
            root = self.balance_node(root)
        return root

#============================

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
        Nodes = [None] * (n + 1)
        for i in range(1, n + 1):
            Nodes[i] = tuple(map(int, f.readline().split()))
        x = int(f.readline())


    tree = AVLTree(n, Nodes)
    tree.root = tree.delete(tree.root, x)

    with open("output.txt", "w") as f:
        f.write(str(tree.number_of_nodes) + '\n')
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
