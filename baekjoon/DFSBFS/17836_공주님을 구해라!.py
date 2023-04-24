from collections import deque

n, m, t = map(int, input().split())
castle = []
gram = False    # 전설의 검 발견 여부
ans = int(1e6)

for _ in range(n):
    castle.append(list(map(int, input().split())))
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque([(0, 0, 0)])
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

while q:
    x, y, cnt = q.popleft()
    if x == n-1 and y == m-1:
        ans = min(cnt, ans)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and castle[nx][ny] == 0: # 이동 가능
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True
            elif castle[nx][ny] == 2:   # 그람 발견
                ans = min(ans, (n-1-nx) + (m-1-ny) + cnt + 1)   # 그람에서 공주님까지 최단 거리
                visited[nx][ny] = True
print(ans if ans <= t else "Fail")