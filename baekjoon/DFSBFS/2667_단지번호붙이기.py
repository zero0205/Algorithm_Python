from collections import deque

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque([[x, y]])
    map_data[x][y] = '0'
    cnt = 1
    
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map_data[nx][ny] == '1':
                    q.append([nx, ny])
                    map_data[nx][ny] = '0'
                    cnt += 1
    return cnt

n = int(input())
map_data = []
ans = []
for _ in range(n):
    map_data.append(list(input()))
    
for i in range(n):
    for j in range(n):
        if map_data[i][j] == '1':
            ans.append(bfs(i, j))

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])