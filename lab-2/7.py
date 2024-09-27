import time
import tracemalloc


def is_bst(tree):
    if not tree:
        return True

    def is_bst_node(index, min_key, max_key):
        if index == -1:
            return True

        key, left_index, right_index = tree[index]
        if min_key > key or key >= max_key:
            return False
        return is_bst_node(left_index, min_key, key) and is_bst_node(right_index, key, max_key)

    return is_bst_node(0, float('-inf'), float('inf'))

def main():
    with open("input7.txt", "r") as f:
        data = f.readlines()
    n = int(data[0])

    tree = []
    for i in range(n):
        node = list(map(int, data[i + 1].split()))
        tree.append((node[0], node[1], node[2]))


    with open("output.txt", "w") as f:
        if is_bst(tree):
            f.write("CORRECT")
        else:
            f.write("INCORRECT")




if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
