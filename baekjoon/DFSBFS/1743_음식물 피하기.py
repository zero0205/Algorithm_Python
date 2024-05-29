from collections import deque

n, m, k = map(int, input().split())
trash = [[False]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    trash[r-1][c-1] = True
visited = [[False]*m for _ in range(n)]


def bfs(x, y):
    res = 1  # 음식물 쓰레기 덩어리의 크기

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and trash[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                res += 1
    return res


ans = 0
for i in range(n):
    for j in range(m):
        if trash[i][j] and not visited[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)
