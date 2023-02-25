from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(input()))
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
q = deque([[0, 0, 1]])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    now_x, now_y, cnt = q.popleft()
    if now_x == n - 1 and now_y == m - 1:
        print(cnt)
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and maze[nx][ny] == '1':
                q.append([nx, ny, cnt + 1])
                visited[nx][ny] = True