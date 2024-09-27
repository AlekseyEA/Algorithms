import time
import tracemalloc

def main():
    with open("input.txt", "r") as f:
        s = [i.strip() for i in f.readlines()]

    with open("output.txt", "w") as f:
        for o in s:
            count = 0
            res = ""
            k, t, p = o.split()
            k = int(k)
            for i in range(len(t) - len(p) + 1):
                error = 0
                for h in range(i, i + len(p)):
                    if p[h - i] != t[h]:
                        error += 1
                        if error > k:
                            break
                if error <= k:
                    count += 1
                    res += str(i) + " "
            f.write(f"{count} {res}\n")


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
