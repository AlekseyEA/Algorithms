import time
import tracemalloc


def passage_of_the_maze(Data, way):
    room = 1
    for color in way:
        room = Data[room][color]
        if room == 0:
            return 'INCORRECT'
    return str(room)


def main():
    with open('input.txt') as f:
        n, m = map(int, f.readline().split())
        Data = [[0]*101 for _ in range(n + 1)]
        for _ in range(m):
            first_room, second_room, color = map(int, f.readline().split())
            Data[first_room][color] = second_room
            Data[second_room][color] = first_room
        f.readline()
        way = map(int, f.readline().split())

    with open("output.txt", "w") as f:
        f.write(passage_of_the_maze(Data, way))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start} секунд")
    print(f"Затраченная память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
