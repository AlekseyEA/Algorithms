import time
import tracemalloc


def find_short_dist(graph, fly_start, fly_end):
    costs = {i: float('inf') for i in graph}
    costs[fly_start] = 0
    visited = set()

    while True:
        min_cost = float('inf')
        current_node = None
        for node in graph:
            if costs[node] < min_cost and node not in visited:
                min_cost = costs[node]
                current_node = node
        if  current_node is None or current_node == fly_end:
            break
        visited.add(current_node)
        for fly_out, fly_in, cost in graph[current_node]:
            if cost + costs[current_node] < costs[fly_in]:
                costs[fly_in] = cost + costs[current_node]
    return costs[fly_end] if costs[fly_end] != float('inf') else -1


def main():
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        Graph = dict({i: [] for i in range(1, n + 1)})
        for i in range(m):
            fly_out, fly_in, cost = map(int, f.readline().split())
            Graph[fly_out].append((fly_out, fly_in, cost))

        fly_out, fly_in = map(int, f.readline().split())

    with open("output.txt", "w") as f:
        f.write(str(find_short_dist(Graph, fly_out, fly_in))) # Используем алгоритм дийкстры



if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
