import time
import tracemalloc


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        lr = sorted([tuple(map(int, f.readline().split())) for _ in range(n)], key=lambda x: x[1])

    count = 0
    sections = []

    for section in lr:
        left, right = section
        if not sections or left > sections[-1]:
            sections.append(right)
            count += 1

    with open("output.txt", "w") as f:
        f.write(f"{count}\n")
        for a in sections:
            f.write(f"{a} ")


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()

