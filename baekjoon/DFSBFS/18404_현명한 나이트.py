from collections import deque

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

n, m = map(int, input().split())
kx, ky = map(int, input().split())  # 나이트 위치

board = [[-1] * (n+1) for _ in range(n+1)]  # 칸별로 도달하는데 필요한 말의 이동 횟수
q = deque([[kx, ky, 0]])
board[kx][ky] = 0

while q:
    x, y, cnt = q.popleft()
    for i in range(8):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] == -1:
            q.append([nx, ny, cnt+1])
            board[nx][ny] = cnt+1

for _ in range(m):
    ex, ey = map(int, input().split())  # 상대편 말 위치
    print(board[ex][ey])