import time
import tracemalloc


def max_cost(a, n, w):
    a.sort(key=lambda k: k[0] / k[1] if k[1] != 0 else 0, reverse=True)
    i = 0
    money = 0
    while w > 0 and i < n:
        if a[i][1] <= w:
            money += a[i][0]
            w -= a[i][1]
        else:
            money += a[i][0] / a[i][1] * w
            w = 0
        i += 1
    return money


def main():
    with open("input.txt") as f:
        n, w = map(int, f.readline().split())
        data = [[0, 0] for _ in range(n)]
        for i in range(n):
            data[i][0], data[i][1] = map(int, f.readline().split())

    money = max_cost(data, n, w)
    with open("output.txt", "w") as f:
        f.write(str(format(money, '.4f')))


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
