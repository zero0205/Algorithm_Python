from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input() for _ in range(r)]


def bfs(x, y):  # (x, y)에서 이동할 수 있는 육지 중 가장 먼 곳까지의 이동 시간
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_dist = 0

    visited = [[False]*c for _ in range(r)]
    visited[x][y] = True
    q = deque([(x, y, 0)])
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
                max_dist = max(max_dist, d+1)
    return max_dist


ans = -1
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)
