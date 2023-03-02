from collections import deque

n, l, r = map(int, input().split())
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

flag = False
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    q = deque([[x, y]])
    visited[x][y] = True
    total = map_data[x][y]
    union = [(x, y)]
    flag = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(map_data[x][y] - map_data[nx][ny]) <= r:
                    flag = True # 인구이동 발생
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    total += map_data[nx][ny]
                    union.append((nx, ny))
    for ux, uy in union:
        map_data[ux][uy] = total // len(union)
        
    return flag

ans = 0
for _ in range(2000):
    flag = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    flag = True
    if not flag:
        break
    ans += 1
    
print(ans)