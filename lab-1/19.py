import time
import tracemalloc


def get_answer(i, j, brackets, res):
    if i == j:
        res += 'A'
        return res
    res += '('
    res = get_answer(i, brackets[i][j], brackets, res)
    res = get_answer(brackets[i][j] + 1, j, brackets, res)
    res += ')'
    return res


def matrix_mult(A, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    brackets = [[0] * (n + 1) for _ in range(n + 1)]

    for right in range(2, n + 1):
        for left in range(right - 1, 0, -1):
            cur = 10 ** 9
            for k in range(left, right):
                cost = dp[left][k] + dp[k + 1][right] + A[left - 1] * A[k] * A[right]
                if cost < cur:
                    cur = cost
                    brackets[left][right] = k
        dp[left][right] = cur
    return get_answer(1, n, brackets, '')


def main():
    with open('input.txt') as f:
        n = int(f.readline())
        A = [tuple(map(int, x.split())) for x in f.readlines()]

    B = [0] * (n + 1)
    for i in range(n):
        B[i] = A[i][0]
    B[n] = A[n - 1][1]
    with open("output.txt", "w") as f:
        f.write(matrix_mult(B, n))


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
