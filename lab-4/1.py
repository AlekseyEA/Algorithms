import time
import tracemalloc


def find_sub_string(sub_string, main_string):
    len_sub_string = len(sub_string)
    len_main_string = len(main_string)
    count = 0
    positions = []
    for i in range(len_main_string - len_sub_string + 1):
        if main_string[i: i + len_sub_string] == sub_string:
            count += 1
            positions.append(i + 1)
    return count, positions


def main():
    with open('input.txt') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    count, positions = find_sub_string(p, t)
    with open("output.txt", "w") as f:
        f.write(f"{count}\n")
        f.write(' '.join(map(str, positions)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
