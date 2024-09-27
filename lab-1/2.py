import time
import tracemalloc


def min_count_stops(x, d, m, n):
    x = [0] + x + [d]
    result = 0
    current_stops = 0
    while current_stops <= n:
        last_stops = current_stops
        while current_stops <= n and x[current_stops + 1] - x[last_stops] <= m:
            current_stops += 1
        if last_stops == current_stops:
            return -1
        if current_stops <= n:
            result += 1
    return result


def main():
    with open('input.txt') as f:
        d = int(f.readline().strip())
        m = int(f.readline().strip())
        n = int(f.readline().strip())
        stop = [int(i) for i in f.readline().split()]
    with open("output.txt", "w") as f:
        f.write(str(min_count_stops(stop, d, m, n)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
