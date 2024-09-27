import time
import tracemalloc


def alchemy(all_reactions, start_reaction, end_reaction):
    len = {}
    len[start_reaction] = 0

    incidents = []
    incidents.append(start_reaction)

    while incidents:
        current = incidents.pop(0)

        if current == end_reaction:
            return len[current]
        if current in all_reactions:
            for next in all_reactions[current]:
                if next not in len:
                    len[next] = len[current] + 1
                    incidents.append(next)
    return -1


def main():
    with open("input.txt", "r") as f:
        m = int(f.readline().strip())
        all_reactions = {}

        for _ in range(m):
            reaction = f.readline().split()
            if reaction[0] in all_reactions:
                all_reactions[reaction[0]].append(reaction[2])
            else:
                all_reactions[reaction[0]] = []
                all_reactions[reaction[0]].append(reaction[2])
        start_reaction = f.readline().strip()
        end_reaction = f.readline().strip()

    with open("output.txt", "w") as f:
        f.write(str(alchemy(all_reactions, start_reaction, end_reaction)))


if __name__ == "__main__":
    tracemalloc.start()
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время: {t_end - t_start} секунд")
    print(f"Память: {tracemalloc.get_traced_memory()}")
    tracemalloc.stop()
