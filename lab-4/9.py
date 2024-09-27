import time
import tracemalloc


def find_decompose(input_str):
    substring = input_str
    builder = []
    start = 0
    while start < len(input_str):
        count = 1
        end = start + 1
        while end < len(input_str):
            substring = input_str[start:end]
            while True:
                next_substring = input_str[start + len(substring):min(end +
                len(substring), len(input_str))]
                if next_substring == substring:
                    count += 1
                    start += len(substring)
                    end += len(substring)
                else:
                    end += 1
                    break
            if count > 1:
                start += len(substring)
                break
        if count > 1:
            if len(substring) * count < len(f'{substring}*{count}+'):
                builder.append(substring * count)
            else:
                if len(builder) > 0 and builder[-1][-1] != '+':
                    builder.append('+')
                builder.append(f"{substring}*{count}+")
        else:
            builder.append(input_str[start])
            start += 1

    result = ''.join(builder)
    if result.endswith('+'):
        return result[:-1]
    else:
        return result


def main():
    with open('input.txt') as f:
        s = f.readline().strip()

    with open("output.txt", "w") as f:
        f.write(find_decompose(s))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
