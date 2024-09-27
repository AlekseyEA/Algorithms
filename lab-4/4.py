import time
import tracemalloc
import random


def precalculate_hashes(s, x, m):
    n = len(s)
    H = [0] * n
    for i in range(1, n):
        H[i] = (x * H[i-1] + ord(s[i])) % m
    return H


def are_equal(s, a, b, l, x, H1, H2, m1, m2):
    p = x**l
    h1_a = (H1[a+l-1] - p * H1[a-1]) % m1
    h2_a = (H2[a+l-1] - p * H2[a-1]) % m2
    h1_b = (H1[b+l-1] - p * H1[b-1]) % m1
    h2_b = (H2[b+l-1] - p * H2[b-1]) % m2
    if h1_a == h1_b and h2_a == h2_b:
        return "Yes"
    return "No"


def main():
    with open('input.txt') as f_input, open("output.txt", "w") as f_output:
        s = f_input.readline().strip()
        q = int(f_input.readline())
        m1 = 10 ** 9 + 7
        m2 = 10 ** 9 + 9
        x = random.randint(1, 10 ** 9)
        H1 = precalculate_hashes(s, x, m1)
        H2 = precalculate_hashes(s, x, m2)
        for _ in range(q):
            a, b, l = map(int, f_input.readline().split())
            f_output.write(are_equal(s, a, b, l, x, H1, H2, m1, m2) + "\n")


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
