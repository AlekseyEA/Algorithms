import time
import tracemalloc


def min_and_max_value(i, j, m, M, operations):
    minimum = float('+inf')
    maximum = float('-inf')
    for k in range(i, j):
        a = eval(M[i][k] + operations[k] + M[k + 1][j])
        b = eval(M[i][k] + operations[k] + m[k + 1][j])
        c = eval(m[i][k] + operations[k] + M[k + 1][j])
        d = eval(m[i][k] + operations[k] + m[k + 1][j])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def get_max_value(digits, operations):
    count_numbers = len(digits)
    m = [[0] * count_numbers for _ in range(count_numbers)]
    M = [[0] * count_numbers for _ in range(count_numbers)]
    for i in range(count_numbers):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1, count_numbers):
        for i in range(count_numbers - s):
            j = i + s
            m[i][j], M[i][j] = map(str, min_and_max_value(i, j, m, M, operations))
    return M[0][count_numbers - 1]


def main():
    with open('input.txt') as f:
        s = f.readline()
        numbers = []
        operations = []
        for i in range(len(s)):
            if i % 2 == 0:
                numbers.append(s[i])
            else:
                operations.append(s[i])

    with open("output.txt", "w") as f:
        f.write(str(get_max_value(numbers, operations)))


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
