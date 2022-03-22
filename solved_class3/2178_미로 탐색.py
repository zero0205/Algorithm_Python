# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())    # m개의 열
    
# 문자열들 숫자로 바꿔주기
maze_int = [[0] * m for _ in range(n)]
for row in range(n):
    for col in range(m):
        maze_int[row][col] = int(maze[row][col])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q=deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 벗어나면 continue
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze_int[nx][ny] == 1:
            maze_int[nx][ny] = maze_int[x][y] + 1
            q.append((nx, ny))

print(maze_int[n-1][m-1])