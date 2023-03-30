from heapq import heappop, heappush

n, k = map(int, input().split())
visited = [False] * 100_001
visited[n] = True
q = []
heappush(q, (0, n))
while q:
    cnt, now = heappop(q)
    if now == k:
        print(cnt)
        break
    if now * 2 <= 100_000 and not visited[now*2]:
        visited[now*2] = True
        heappush(q, (cnt, now*2))
    for nx in [now-1, now+1]:
        if 0 <= nx <= 100_000 and not visited[nx]:
            visited[nx] = True
            heappush(q, (cnt+1, nx))