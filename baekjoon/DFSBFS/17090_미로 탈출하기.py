import sys
sys.setrecursionlimit(10000000)


def dfs(x, y):
    visited[x][y] = 0
    if maze[x][y] == 'U':
        nx, ny = x-1, y
    elif maze[x][y] == 'R':
        nx, ny = x, y+1
    elif maze[x][y] == 'D':
        nx, ny = x+1, y
    elif maze[x][y] == 'L':
        nx, ny = x, y-1

    if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 탈출
        visited[x][y] = 1
    elif visited[nx][ny] == -1:  # 아직 방문 안 한 칸
        visited[x][y] = dfs(nx, ny)
    else:                       # 이미 방문한 칸
        visited[x][y] = visited[nx][ny]

    return visited[x][y]


n, m = map(int, input().split())
maze = []
visited = [[-1] * m for _ in range(n)]
for _ in range(n):
    maze.append(list(input()))

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            dfs(i, j)

ans = 0
for i in range(n):
    ans += sum(visited[i])
print(ans)
