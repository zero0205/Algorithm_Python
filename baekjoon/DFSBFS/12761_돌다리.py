from collections import deque

a, b, n, m = map(int, input().split())

q = deque([(n, 0)])
visited = [False] * 100_001
visited[n] = True

while q:
    now, cnt = q.popleft()
    if now == m:
        print(cnt)
        break
    for nx in [now+1, now-1, now+a, now-a, now+b, now-b, now*a, now*b]:
        if nx < 0 or nx > 100_000:
            continue
        if not visited[nx]:
            q.append((nx, cnt+1))
            visited[nx] = True
