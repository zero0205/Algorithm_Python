from collections import deque

m, n, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1, x2):
        for c in range(y1, y2):
            board[r][c] = 1

def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]  
    
    q = deque([(x, y)])
    board[x][y] = -1    # 방문 처리
    res = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = -1
                res+=1
    return res

rectangles = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            rectangles.append(bfs(i, j))
print(len(rectangles))
print(*sorted(rectangles))
