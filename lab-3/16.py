def find_cycle(u, f, g, mp):
    if u in mp and mp[u] == f:
        return u == f
    mp[u] = f
    for v in g[u]:
        if find_cycle(v, f, g, mp):
            return True
    return False


with open("input.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]
index = 0
V = int(data[index])
index += 1

g = {}
name = []
mp = {}

for _ in range(V):
    u = data[index]
    index += 1
    E = int(data[index])
    index += 1
    name.append(u)
    g[u] = []
    for _ in range(E):
        v = data[index]
        index += 1
        g[u].append(v)
    index += 1

with open("output.txt", "w") as f:
    for p in name:
        mp.clear()
        f.write("YES\n" if find_cycle(p, p, g, mp) else "NO\n")

