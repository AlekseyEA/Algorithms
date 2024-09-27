import time
import tracemalloc


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



class BinTree:
    def __init__(self):
        self.root = None
        self.pred = None


    def ins(self, x, root):
        if root is None:
            return Node(x)
        if x < root.key:
            root.left = self.ins(x, root.left)
        elif x > root.key:
            root.right = self.ins(x, root.right)
        return root


    def delete(self, x, root):
        if root is None:
            return None
        if x < root.key:
            root.left = self.delete(x, root.left)
        elif x > root.key:
            root.right = self.delete(x, root.right)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                next_root = self.find_min(root.right)
                root.key = next_root.key
                root.right = self.delete(next_root.key, root.right)
        return root

    def exist(self, x, root):
        if root is None:
            return False
        if x < root.key:
            return self.exist(x, root.left)
        elif x > root.key:
            return self.exist(x, root.right)
        else:
            return True

    def find_min(self, root):
        while root and root.left:
            root = root.left
        return root

    def find_max(self, root):
        while root and root.right:
            root = root.right
        return root

    def next(self, x, root):
        if root is None:
            return None
        successor = None
        while root:
            if root.key > x:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor.key if successor else None

    def prev(self, x, root):
        if root is None:
            return None
        predecessor = None
        while root:
            if root.key < x:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor.key if predecessor else None

    def insert(self, x):
        self.root = self.ins(x, self.root)

    def delete_key(self, x):
        self.root = self.delete(x, self.root)

    def exists(self, x):
        return self.exist(x, self.root)

    def next_key(self, x):
        return self.next(x, self.root)

    def prev_key(self, x):
        return self.prev(x, self.root)


def main():
    with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
        bin_tree = BinTree()
        for line in input_file:
            command, x = line.strip().split()
            x = int(x)
            if command == "insert":
                bin_tree.insert(x)
            elif command == "delete":
                bin_tree.delete_key(x)
            elif command == "exists":
                output_file.write("true\n" if bin_tree.exists(x) else "false\n")
            elif command == "next":
                result = bin_tree.next_key(x)
                output_file.write(f"{result}\n" if result is not None else "none\n")
            elif command == "prev":
                result = bin_tree.prev_key(x)
                output_file.write(f"{result}\n" if result is not None else "none\n")


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start} секунд")
    print(f"Затраченная память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
