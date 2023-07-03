from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(input())
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()
visited = [[False] * n for _ in range(m)]
for i in range(n):
    if board[0][i] == '0':
        q.append((0, i))
        visited[0][i] = True
        
while q:
    x, y = q.popleft() 
    if x == m-1:
        print("YES")
        exit()
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i] 
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == '0':
                q.append((nx, ny))
                visited[nx][ny] = True
print("NO")