# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j)) # 익은 토마토가 들어있는 칸
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if tomato[nx][ny] == 0:
            q.append((nx, ny))
            tomato[nx][ny] = tomato[x][y] + 1   # 익는데 걸린 일수 + 1

flag = False
max_value = 0
for i in range(n):
    if flag:
        break
    for j in range(m):
        if tomato[i][j] == 0:
            flag = True
            break
        max_value = max(max_value, tomato[i][j])
        
if flag:
    print(-1)
else:
    print(max_value - 1)