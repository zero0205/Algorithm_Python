from itertools import combinations
from collections import deque

n, m = map(int, input().split())
board = []
virus_pos = []
for i in range(n):
    # 0은 빈 칸, 1은 벽, 2는 바이러스 놓을 수 있는 칸
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 2:
            virus_pos.append((i, j))


def bfs(virus):
    max_time = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[-1]*n for _ in range(n)]
    for v in virus:
        visited[v[0]][v[1]] = 0
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and board[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    max_time = max(max_time, visited[nx][ny])
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 0 or board[i][j] == 2) and visited[i][j] == -1:
                return 2500

    return max_time


ans = 2500
for comb in combinations(virus_pos, m):
    ans = min(bfs(comb), ans)

print(ans if ans < 2500 else -1)
