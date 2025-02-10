from collections import deque

n = int(input())
rooms = [input() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0)])
visited = [[int(1e9)]*n for _ in range(n)]
visited[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if rooms[nx][ny] == "0" and visited[nx][ny] > visited[x][y]+1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx, ny))
            elif rooms[nx][ny] == "1" and visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))

print(visited[n-1][n-1])
