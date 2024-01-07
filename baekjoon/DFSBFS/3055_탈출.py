from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

hx, hy = -1, -1
ans = int(1e6)

# 고슴도치 초기 위치
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':    # 고슴도치
            hx, hy = i, j

# 구역당 물이 차는데 걸리는 시간 구하기
water = [[int(1e6)]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':  # 물이 차 있는 지역
            water[i][j] = 0
            # BFS
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                        if water[nx][ny] > water[x][y]+1:
                            water[nx][ny] = water[x][y]+1
                            q.append((nx, ny))

# BFS
q = deque([(hx, hy, 0)])
board[hx][hy] = '*'  # 이미 고슴도치가 지나간 곳 '*'으로 표시
while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] == '.' and water[nx][ny] > cnt+1:
                q.append((nx, ny, cnt+1))
                board[nx][ny] = '*'
            elif board[nx][ny] == 'D':  # 비버의 굴 도착
                print(cnt+1)
                exit()
print("KAKTUS")
