import heapq

n, k = map(int, input().split())
visited = [False] * 100_001

q = [(0, n)]
while True:
    cnt, now = heapq.heappop(q)
    if now == k:
        print(cnt)
        break
    visited[now] = True
    if now * 2 <= 100_000 and not visited[now*2]:
        heapq.heappush(q, (cnt, now*2))
    for i in [now-1, now+1]:
        if 0 <= i <= 100_000 and not visited[i]:
            heapq.heappush(q, (cnt+1, i))