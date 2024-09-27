import time
import tracemalloc


def first_dfs(graph, v, visited, attended):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            first_dfs(graph, i, visited, attended)
    attended.append(v)

def second_dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            second_dfs(graph, i, visited)

# ============================

def transpose_graph(graph, n):
    new_graph = dict({i: [] for i in range(1, n + 1)})
    for i in graph:
        for j in graph[i]:
            new_graph[j].append(i)
    return new_graph

# ============================

def count_components(n, Graph):
    attended = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
           first_dfs(Graph, i, visited, attended)

    gr = transpose_graph(Graph, n)

    visited = [False] * (n + 1) #очищаем visited
    count = 0
    while attended:
        i = attended.pop()
        if not visited[i]:
            second_dfs(gr, i, visited)
            count += 1
    return count


def main():
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        Graph = dict({i: [] for i in range(1, n + 1)})
        for _ in range(m):
            u, v = map(int, f.readline().split())
            Graph[u].append(v)

    with open("output.txt", "w") as f:
        f.write(str(count_components(n, Graph)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
