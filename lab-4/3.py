import time
import tracemalloc
import random


def poly_hash(S, p, x):
    h = 0
    for i in range(len(S)):
        h += ord(S[i]) * (x ** i)
    return h % p


def precalculate_hashes(T, P, p, x):
    len_t = len(T)
    len_p = len(P)
    H = [0] * (len_t - len_p + 1)
    S = T[len_t - len_p:len_t]
    H[len_t - len_p] = poly_hash(S, p, x)

    y = 1
    for i in range(len_p):
        y = (y * x) % p
    for i in range(len_t - len_p - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len_p])) % p
    return H


def alg_rabin_karp(T, P):
    p = 10 ** 9 + 9
    x = random.randint(1, p - 1)
    result = []
    pol_hash = poly_hash(P, p, x)
    H = precalculate_hashes(T, P, p, x)
    for i in range(len(T) - len(P) + 1):
        if pol_hash != H[i]:
            continue
        if T[i:i + len(P)] == P:
            result.append(i + 1)

    return result


def main():
    with open('input.txt') as f:
        P = f.readline().strip()
        T = f.readline().strip()

    indexes = alg_rabin_karp(T, P)
    with open("output.txt", "w") as f:
        f.write(f"{len(indexes)}\n")
        f.write(" ".join(map(str, indexes)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
