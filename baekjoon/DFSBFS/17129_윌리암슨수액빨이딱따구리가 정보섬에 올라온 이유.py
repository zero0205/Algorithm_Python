import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map_data = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if map_data[i][j] == "2":
            start = [i, j]
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([[*start, 0]])
visited = [[False]*m for _ in range(n)]
visited[start[0]][start[1]] = True
while q:
    x, y, d = q.popleft()
    if map_data[x][y] in ["3", "4", "5"]:
        print("TAK\n{}".format(d))
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map_data[nx][ny] != "1":
            q.append([nx, ny, d+1])
            visited[nx][ny] = True
print("NIE")
