from collections import defaultdict

n = int(input())
m = int(input())

adj_list = defaultdict(list)
visitados = set()
low = [-1] * (n + 1)
disc = [-1] * (n + 1)
timer = [1]
articulation_points = set()


while m > 0:
    u, v = map(int, input().split())
    adj_list[int(u)].append(int(v))
    adj_list[int(v)].append(int(u))
    m -= 1


def tarjan(nodo_actual, padre):
    visitados.add(nodo_actual)
    low[nodo_actual] = timer[0]  # noqa: F823
    disc[nodo_actual] = timer[0]
    timer[0] += 1  # noqa: F841
    child = 0

    for v in adj_list[nodo_actual]:
        if v == padre:
            continue
        if v not in visitados:
            child += 1
            tarjan(v, nodo_actual)
            low[nodo_actual] = min(low[nodo_actual], low[v])
            if padre != -1 and low[v] >= disc[nodo_actual]:
                articulation_points.add(nodo_actual)
        else:
            low[nodo_actual] = min(low[nodo_actual], disc[v])
    if padre == -1 and child > 1:
        articulation_points.add(nodo_actual)

for i in range(1, n + 1):
    if i not in visitados:
        tarjan(i, -1)
print(articulation_points)
