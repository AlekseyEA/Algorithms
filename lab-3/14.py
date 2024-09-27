import time
import tracemalloc


def find_short_time(graph, start_pos, end_pos):
    distances = {i: float('inf') for i in graph}
    distances[start_pos] = 0
    visited = set()

    while True:
        min_distance = float('inf')
        current_node = None
        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                current_node = node
        if current_node is None or current_node == end_pos:
            break
        visited.add(current_node)
        for start_place, leaving_time, end_position, coming_time in graph[current_node]:
            if leaving_time >= distances[current_node] and coming_time < distances[end_position]:
                distances[end_position] = coming_time
    return distances[end_pos] if distances[end_pos] != float('inf') else -1


def main():
    with open('input.txt') as f:
        N = int(f.readline().strip())
        d, v = map(int, f.readline().strip().split())
        R = int(f.readline().strip())
        bus_schedule = {i: [] for i in range(1, N + 1)}
        for _ in range(R):
            start_place, leaving_time, finish_place, coming_time = map(int, f.readline().split())
            bus_schedule[start_place].append((start_place, leaving_time, finish_place, coming_time))

    with open("output.txt", "w") as f:
        f.write(str(find_short_time(bus_schedule, d, v)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
