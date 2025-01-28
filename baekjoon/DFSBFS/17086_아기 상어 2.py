from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(x, y):
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y, 0)])
    while q:
        now_x, now_y, cnt = q.popleft()
        if map_data[now_x][now_y] == 1:
            return cnt
        for i in range(8):
            nx = now_x + dir[i][0]
            ny = now_y + dir[i][1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True


answer = 0
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 0:
            res = bfs(i, j)
            answer = max(answer, res)
print(answer)
