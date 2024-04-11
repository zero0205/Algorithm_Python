from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
roads = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((c, b))
    roads[b].append((c, a))

# Dijkstra
dist = [sys.maxsize]*n  # y에서 각 집까지의 최단 거리
dist[y] = 0
q = [(0, y)]

while q:
    d, now = heappop(q)
    for nd, nx in roads[now]:
        if dist[nx] > dist[now]+nd:  # now를 거쳐서 nx로 가는 것이 더 최단 거리인 경우
            heappush(q, (dist[now]+nd, nx))
            dist[nx] = dist[now]+nd

dist.sort()  # 오름차순 정렬
if dist[-1] > x:
    print(-1)
else:
    tmp = 0
    ans = 0
    for d in dist:
        if tmp+d*2 <= x:
            tmp += d*2
        else:
            ans += 1
            tmp = d*2
    print(ans+(1 if tmp > 0 else 0))
