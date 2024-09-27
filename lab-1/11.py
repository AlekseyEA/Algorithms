import time
import tracemalloc


def max_count_gold(capacity, weights):
    dp = [1] + [0] * capacity

    max_index = 0
    for weight in weights:
        index_weight = capacity
        while index_weight - weight >= 0:
            if dp[index_weight - weight] == 1:
                dp[index_weight] = 1
                max_index = max(max_index, index_weight)
            index_weight -= 1
    return max_index


def main():
    with open('input.txt') as f:
        capacity, n = map(int, f.readline().split())
        weights = [int(weight) for weight in f.readline().split()]

    with open("output.txt", "w") as f:
        f.write(str(max_count_gold(capacity, weights)))


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()

    main()

    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
