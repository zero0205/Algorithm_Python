import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
            if visited[nx][ny] == 0:
                dfs(nx, ny)
            visited[x][y] = max(visited[nx][ny]+1, visited[x][y])


ans = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
for i in range(n):
    for j in range(n):
        ans = max(ans, visited[i][j])
print(ans)
