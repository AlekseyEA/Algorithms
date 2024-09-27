import time
import tracemalloc


def height(nodes, index_node):
    if index_node == 0:
        return 0
    return nodes[index_node][3]


def check_balance(nodes, index_node):
    if index_node == 0:
        return

    check_balance(nodes, nodes[index_node][1]) #check left
    check_balance(nodes, nodes[index_node][2]) #check right

    nodes[index_node][3] = 1 + max(height(nodes, nodes[index_node][1]), height(nodes, nodes[index_node][2])) #получение высоты
    nodes[index_node][4] = height(nodes, nodes[index_node][2]) - height(nodes, nodes[index_node][1]) #получение разницы


def main():
    with open("input.txt") as f:
        n = int(f.readline())
        data = f.readlines()

        Nodes = [None] * (n + 1)
        for i, node in enumerate(data, 1):
            Nodes[i] = list(map(int, node.split())) + [1, 0] #[1, 0] для высот

    if n != 0:
        check_balance(Nodes, 1)

    with open("output.txt", "w") as f:
        for node in Nodes[1:]:
            f.write(str(node[4]) + '\n')


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
