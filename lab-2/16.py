import time
import tracemalloc

result = []

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def node_find(self, node, parent, key):
        if node is None:
            return None, parent, False

        if key == node.key:
            return node, parent, True

        if key < node.key:
            if node.left:
                return self.node_find(node.left, node, key)
        if key > node.key:
            if node.right:
                return self.node_find(node.right, node, key)

        return node, parent, False


    def node_find_min(self, node, p):
        if node.left:
            return self.node_find_min(node.left, node)
        return node, p

# ============================

    def append(self, node):
        if self.root is None:
            self.root = node
            return node

        root, parent, key_find = self.node_find(self.root, None, node.key)
        if not key_find and root:
            if node.key < root.key:
                root.left = node
            else:
                root.right = node

        return node

# ============================

    def delete_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def delete_node(self, key):
        s, p, fl_find = self.node_find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            if p:
                if p.left == s:
                    p.left = None
                elif p.right == s:
                    p.right = None
            else:
                self.root = None
        elif s.left is None or s.right is None:
            self.delete_child(s, p)
        else:
            sr, pr = self.node_find_min(s.right, s)
            s.key = sr.key
            self.delete_child(sr, pr)

# ============================

    def get_ki_max(self, key):
        self.get_ki(self.root, key, 0)

    def get_ki(self, node, key, index):
        if node is None:
            return index
        index = self.get_ki(node.right, key, index)
        index += 1
        if index == key:
            result.append(str(node.key))
            return index
        return self.get_ki(node.left, key, index)


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    n = int(data[0])
    tree = Tree()
    for i in range(n):
        s = data[i + 1].split()
        if s[0] == "+1" or s[0] == "1":
            tree.append(Node(int(s[1])))
        elif s[0] == "0":
            tree.get_ki_max(int(s[1]))
        else:
            tree.delete_node(int(s[1]))

    with open("output.txt", "w") as f:
        f.write("\n".join(result))


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
