# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())

map_data = []
for _ in range(n):
    map_data.append(input())
    
map_int = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        map_int[i][j] = int(map_data[i][j])
    
def bfs(r, c, map_data):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num = 1
    q = deque([(r, c)])
    map_data[r][c] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = 0
                q.append((nx, ny))
                num += 1
    return num

total = 0
arr = []
for i in range(n):
    for j in range(n):
        if map_int[i][j] == 1:
            total += 1
            arr.append(bfs(i, j, map_int))
arr.sort()
print(total)
for i in range(total):
    print(arr[i])