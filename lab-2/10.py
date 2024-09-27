import sys, threading
sys.setrecursionlimit(2147483647)
import time
import tracemalloc


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.left_bord = -sys.maxsize
        self.right_bord = sys.maxsize

def checkTree(bin_tree, i):
    # print(f"chT Key: {bin_tree[i].key} left {bin_tree[i].left} right {bin_tree[i].right} l_bord {bin_tree[i].left_bord} r_bord {bin_tree[i].right_bord}")
    if bin_tree[i].left != -1 and bin_tree[i].key < bin_tree[bin_tree[i].left].key:
        return False
    if bin_tree[i].right != -1 and bin_tree[i].key > bin_tree[bin_tree[i].right].key:
        return False

    if bin_tree[i].key <= bin_tree[i].left_bord:
        return False
    if bin_tree[i].key >= bin_tree[i].right_bord:
        return False

    if bin_tree[i].left != -1:
        # print(" l_b_m ")
        bin_tree[bin_tree[i].left].left_bord = bin_tree[i].left_bord
        bin_tree[bin_tree[i].left].right_bord = bin_tree[i].key

    if bin_tree[i].right != -1:
        # print(" r_b_m ")
        bin_tree[bin_tree[i].right].left_bord = bin_tree[i].key
        bin_tree[bin_tree[i].right].right_bord = bin_tree[i].right_bord

    if bin_tree[i].left != -1 and not checkTree(bin_tree, bin_tree[i].left):
        # print("l_fal")
        return False
    if bin_tree[i].right != -1 and not checkTree(bin_tree, bin_tree[i].right):
        # print("r_fal")
        return False

    return True

def main():
    with open("input.txt", "r") as input_file:
        n = int(input_file.readline().strip())
        if n == 0:
            with open("output.txt", "w") as output_file:
                output_file.write("YES")
            return

        bin_tree = []
        for _ in range(n):
            k, l, r = map(int, input_file.readline().strip().split())
            bin_tree.append(Node(k, l-1, r-1))

    if checkTree(bin_tree, 0):
        with open("output.txt", "w") as output_file:
            output_file.write("YES")
    else:
        with open("output.txt", "w") as output_file:
            output_file.write("NO")

if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    thread = threading.Thread(target=main())
    thread.start()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start} секунд")
    print(f"Затраченная память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
