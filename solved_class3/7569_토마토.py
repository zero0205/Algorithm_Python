# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int,sys.stdin.readline().split())))

q = deque()
for height in range(h):
    for row in range(n):
        for col in range(m):
            if tomato[height][row][col] == 1:
                q.append((height, row, col)) # 익은 토마토가 들어있는 칸

dh = [-1, 1, 0, 0, 0, 0]            
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while q:
    l, x, y = q.popleft()
    for i in range(6):
        nl = l + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nl < h and 0 <= nx < n and 0 <= ny < m):
            continue
        if tomato[nl][nx][ny] == 0:
            q.append((nl, nx, ny))
            tomato[nl][nx][ny] = tomato[l][x][y] + 1   # 익는데 걸린 일수 + 1

flag = False
max_value = 0
for k in range(h):
    if flag:
        break
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                flag = True
                break
            max_value = max(max_value, tomato[k][i][j])

if flag:
    print(-1)
else:
    print(max_value - 1)