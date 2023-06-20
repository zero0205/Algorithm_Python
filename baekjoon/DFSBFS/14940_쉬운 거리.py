from collections import deque

n, m = map(int, input().split())
map_data = []
dist = [[-1] * m for _ in range(n)]
dest_x, dest_y = 0, 0
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 0:
            dist[i][j] = 0
        if lst[j] == 2:
            dest_x, dest_y = i, j
            dist[dest_x][dest_y] = 0
    map_data.append(lst)
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]
q = deque([[dest_x, dest_y, 0]])
visited[dest_x][dest_y] = True

while q:
    x, y, d = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if map_data[nx][ny] == 0:
                dist[nx][ny] = 0
            if map_data[nx][ny] == 1 and not visited[nx][ny]:
                dist[nx][ny] = d + 1
                q.append([nx, ny, d+1])
                visited[nx][ny] = True

for i in range(n):
    print(*dist[i])