from collections import deque

n = int(input())
a = list(map(int, input().split()))
start = int(input())-1

q = deque([start])
visited = [False]*n
visited[start] = True
ans = 1
while q:
    now = q.popleft()
    # 왼쪽, 오른쪽
    for nx in [now-a[now], now+a[now]]:
        if 0 <= nx < n and not visited[nx]:
            visited[nx] = True
            q.append(nx)
            ans += 1
print(ans)
