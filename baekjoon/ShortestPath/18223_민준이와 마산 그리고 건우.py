from heapq import heappop, heappush

v, e, p = map(int, input().split())
edges = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))


def dijkstra(s, e):
    q = [(0, s)]
    dist = [int(1e9)]*(v+1)
    dist[s] = 0
    while q:
        nd, nn = heappop(q)
        for next, cost in edges[nn]:
            if nd+cost < dist[next]:
                heappush(q, (nd+cost, next))
                dist[next] = nd+cost
    return dist[e]


if dijkstra(1, p)+dijkstra(p, v) <= dijkstra(1, v):
    print("SAVE HIM")
else:
    print("GOOD BYE")
