from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    road[a].append((b, d*2))
    road[b].append((a, d*2))

# 여우
fox_dist = [int(1e9)] * (n+1)
hq = [(0, 1)]
while hq:
    now_d, now = heappop(hq)
    if fox_dist[now] < now_d:
        continue
    for nx, nx_d in road[now]:
        cost = now_d + nx_d
        if fox_dist[nx] > cost:  # now 거쳐서 nx 가는게 더 빠른 경우
            fox_dist[nx] = cost
            heappush(hq, (cost, nx))

# 늑대
wolf_dist = [[int(1e9)]*2 for _ in range(n+1)]
hq = [(0, 1, True)]
while hq:
    now_d, now, fast = heappop(hq)
    # now->nx로 2배 속도로 움직임
    if fast:
        if wolf_dist[now][1] < now_d:
            continue
        for nx, nx_d in road[now]:
            cost = now_d + nx_d // 2
            if wolf_dist[nx][0] > cost:
                wolf_dist[nx][0] = cost
                heappush(hq, (cost, nx, False))
    # now->nx로 0.5배 속도로 움직임
    else:
        if wolf_dist[now][0] < now_d:
            continue
        for nx, nx_d in road[now]:
            cost = now_d + nx_d * 2
            if wolf_dist[nx][1] > cost:
                wolf_dist[nx][1] = cost
                heappush(hq, (cost, nx, True))

ans = 0
for i in range(2, n+1):
    if fox_dist[i] < wolf_dist[i][0] and fox_dist[i] < wolf_dist[i][1]:
        ans += 1
print(ans)
