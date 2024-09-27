import time
import tracemalloc


def get_answer(dp, pred, s, left, right, res):
    if right == left:
        pass
    elif dp[left][right] == 0:
        for k in range(left, right + 1):
            res += s[k]
    elif pred[left][right] == -1:
        res += s[left]
        res = get_answer(dp, pred, s, left + 1, right - 1, res)
        res += s[right]
    else:
        res = get_answer(dp, pred, s, left, pred[left][right], res)
        res = get_answer(dp, pred, s, pred[left][right] + 1, right, res)
    return res


def remove_brackets(s):
    maxsize = 101
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    pred = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for right in range(1, n):
        for left in range(right - 1, -1, -1):
            if (s[left] == '(' and s[right] == ')') or (s[left] == '[' and s[right] == ']') or (s[left] == '{' and s[right] == '}'):
                cur = dp[left + 1][right - 1]
            else:
                cur = maxsize
            pred[left][right] = -1
            for k in range(left, right):
                if dp[left][k] + dp[k + 1][right] < cur:
                    cur = dp[left][k] + dp[k + 1][right]
                    pred[left][right] = k

            dp[left][right] = cur
    return get_answer(dp, pred, s, 0, n - 1, '')


def main():
    with open('input.txt') as f:
        s = f.readline()

    with open("output.txt", "w") as f:
        f.write(remove_brackets(s))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
