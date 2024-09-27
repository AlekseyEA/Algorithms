import time
import tracemalloc


def treasure(string):
    i = 0

    while i < len(string):
        if string[i] == ' ':
            string = string[:i] + string[i + 1:]
        else:
            i += 1

    prev_chars = {}
    char_tup = [(0, 0) for _ in range(len(string))]

    for i in range(len(string)):
        if string[i] in prev_chars:
            prev_index = prev_chars[string[i]]
            prev_state = char_tup[prev_index]
            char_tup[i] = (prev_state[0] + 1, prev_state[1] + (i - 1 - prev_index) + (prev_state[0] * (i - prev_index)))
        prev_chars[string[i]] = i

    result = 0
    for state in char_tup:
        result += state[1]
    return result


def main():
    with open('input.txt') as f:
        string = f.readline().strip()

    with open("output.txt", "w") as f:
        f.write(str(treasure(string)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
