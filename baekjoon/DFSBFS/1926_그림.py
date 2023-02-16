from collections import deque

n, m = map(int, input().split())
picture = []
for _ in range(n):
    picture.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    area = 1
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if picture[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1
    return area

visited = [[False for _ in range(m)] for _ in range(n)]
num = 0
ans = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            a = bfs(i, j, visited)
            num += 1
            ans = max(ans, a)
            
print(num)
print(ans)