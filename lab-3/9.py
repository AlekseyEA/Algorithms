import time
import tracemalloc


def bellman_ford(graph, n):
    distance = [float("inf")] * (n + 1)
    distance[1] = 0
    for _ in range(n - 1):
        for u, v, value in graph:
            if distance[u] != float("inf") and distance[u] + value < distance[v]:
                distance[v] = distance[u] + value

    for u, v, value in graph:
        if distance[u] != float("inf") and distance[u] + value < distance[v]:
            return False
    return True


def main():
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        graph = []
        for _ in range(m):
            graph.append(tuple(map(int, f.readline().split())))

    with open("output.txt", "w") as f:
        if bellman_ford(graph, n):  # используем алгоритм Беллмана-Форда
            f.write('0')
        else:
            f.write('1')


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
