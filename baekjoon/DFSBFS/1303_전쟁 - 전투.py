from collections import deque

n, m = map(int, input().split())
board = [input() for _ in range(m)]
visited = [[False]*n for _ in range(m)]
power = {"W": 0, "B": 0}  # 각 나라의 병사의 위력의 합


def bfs(x, y, color):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(x, y)])
    cnt = 1
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            power[board[i][j]] += bfs(i, j, board[i][j])**2

print(*power.values())
