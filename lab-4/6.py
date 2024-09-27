import time
import tracemalloc


def z_function(s):
    z_f = [0] * len(s)
    left = right = 0
    for i in range(1, len(s)):
        z_f[i] = max(0, min(right - i, z_f[i - left]))
        while i + z_f[i] < len(s) and s[z_f[i]] == s[i + z_f[i]]:
            z_f[i] += 1
        if i + z_f[i] > right:
            left = i
            right = i + z_f[i]
    return z_f[1:]


def main():
    with open('input.txt') as f:
        s = f.readline()

    with open("output.txt", "w") as f:
        f.write(' '.join(map(str, z_function(s))))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
