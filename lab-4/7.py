#переписать
#не работает

import time
import tracemalloc
import random


def poly_hash_1(S, p, x):
    h = 0
    for i in range(len(S)):
        h += ord(S[i]) * (x**i)
    return h % p


def poly_hash_2(S, p, x):
    h = 0
    for i in range(len(S)):
        h += (ord(S[i]) - 65) * (x**(i+1))
    return h % p


def exist(s, t, i, p, x):
    if i == 0:
        return (True, 0, 0)

    hashes_set_1 = set()
    hashes_set_2 = set()
    hashes = [0] * (len(s) - i + 1)
    for j in range(len(s) - i + 1):
        h1 = poly_hash_1(s[j:j + i], p, x)
        h2 = poly_hash_2(s[j:j + i], p, x)
        hashes_set_1.add(h1)
        hashes_set_2.add(h2)
        hashes[j] = (j, h1)

    for j in range(len(t) - i + 1):
        hash1 = poly_hash_1(t[j:j+i], p, x)
        hash2 = poly_hash_2(t[j:j+i], p, x)
        if hash1 in hashes_set_1 and hash2 in hashes_set_2:
            for h in hashes:
                if h[1] == hash1:
                    if not (t[j:j+i] == s[h[0]:h[0]+i]):
                        continue
                    return (True, h[0], j)

    return (False, 0, 0)


def biggest_common_substr(s, t):
    p = 10 ** 9 + 9
    x = random.randint(1, p - 1)
    answer = 0
    low, high = 0, min(len(s), len(t))
    while low <= high:
        mid = (low + high) // 2
        ex = exist(s, t, mid, p, x)
        if ex[0]:
            answer = (ex[1], ex[2], mid)
            low = mid + 1
        else:
            high = mid - 1
    return answer


def main():
    with open('input.txt') as f_input, open("output.txt", "w") as f_output:
        for string in f_input.readlines():
            s, t = string.split()
            f_output.write(' '.join(map(str, biggest_common_substr(s, t))) + '\n')




if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
