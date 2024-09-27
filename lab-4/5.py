import time
import tracemalloc


def prefix_function(s):
    P = [0] * (len(s) + 1)
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            P[i+1] = j + 1
            i += 1
            j += 1
        else:
            if j <= 0:
                P[i + 1] = 0
                i += 1
            else:
                j = P[j]
    return P[1:]



def main():
    with open('input.txt') as f:
        s = f.readline()

    with open("output.txt", "w") as f:
        f.write(' '.join(map(str, prefix_function(s))))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
