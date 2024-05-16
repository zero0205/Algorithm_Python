from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        heappush(graph[b], (s, a))
    # Dijkstra
    dist = [int(1e9)] * (n+1)   # 근원지에서 다른 모든 컴퓨터까지 걸리는 시간
    dist[c] = 0  # 근원지
    hq = [(0, c)]
    while hq:
        t, now = heappop(hq)
        if dist[now] < t:
            continue
        for ns, nx in graph[now]:
            if t+ns < dist[nx]:
                dist[nx] = t+ns
                heappush(hq, (t+ns, nx))
    ans = [0, 0]
    for i in range(1, n+1):
        if dist[i] != int(1e9):
            ans[0] += 1
            if dist[i] > ans[1]:
                ans[1] = dist[i]
    print(*ans)
