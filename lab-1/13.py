import time
import tracemalloc


def is_possible_to_split_souvenirs(souvenirs, n, sum1, sum2, sum3, index, data):
    if index == n:
        if sum1 == sum2 == sum3:
            return '1'
        else:
            return '0'

    key = (sum1, sum2, sum3, index)
    if key in data:
        return data[key]
    data[key] = max(
        is_possible_to_split_souvenirs(souvenirs, n, sum1 + souvenirs[index], sum2, sum3, index + 1, data),
        is_possible_to_split_souvenirs(souvenirs, n, sum1, sum2 + souvenirs[index], sum3, index + 1, data),
        is_possible_to_split_souvenirs(souvenirs, n, sum1, sum2, sum3 + souvenirs[index], index + 1, data)
    )
    return data[key]


def main():
    with open('input.txt') as f:
        n = int(f.readline())
        souvenirs = [int(souvenir) for souvenir in f.readline().split()]

    with open("output.txt", "w") as f:
        if sum(souvenirs) % 3 == 0:
            f.write(is_possible_to_split_souvenirs(souvenirs, n, 0, 0, 0, 0, {}))
        else:
            f.write('0')


if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()

    main()
    t_end = time.perf_counter()
    print(f'Время: {t_end - t_start} секунд')
    print(f'Память: {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()
