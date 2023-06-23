import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
cheeze = []
for _ in range(r):
    cheeze.append(list(map(int, input().split())))
    
all_melt = False
sec = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

prev_cheeze = 0

while True:
    sec += 1
    remain_cheeze = 0
    
    q = deque([(0, 0)])
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if cheeze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1 and not visited[nx][ny]:   # 공기와 접촉한 치즈
                    remain_cheeze += 1
                    visited[nx][ny] = True
                    cheeze[nx][ny] = 0  # 치즈 녹음
    if remain_cheeze == 0:
        print(sec)
        print(prev_cheeze)
        break
    else:
        prev_cheeze = remain_cheeze