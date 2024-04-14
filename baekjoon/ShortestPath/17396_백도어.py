from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
visible = list(map(int, input().split()))
visible[n-1] = 0
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# Dijkstra
time = [INF]*n
time[0] = 0
q = [(0, 0)]
while q:
    t, now = heappop(q)
    if t > time[now]:   # time[now]가 t보다 더 빠른 시간으로 이미 갱신된 경우
        continue
    for nx, c in graph[now]:
        if visible[nx] == 0 and time[nx] > time[now]+c:
            time[nx] = time[now]+c
            heappush(q, (time[now]+c, nx))
print(time[n-1] if time[n-1] != INF else -1)
