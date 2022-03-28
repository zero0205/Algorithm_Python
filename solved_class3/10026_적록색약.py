# https://www.acmicpc.net/problem/10026

from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def color(x, y, map_data, visited):
    q = deque([(x, y)])
    co = map_data[x][y]
    visited[x][y] = True
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if map_data[nr][nc] == co:
                if not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                
def colorless(x, y, map_data, visited):
    q = deque([(x, y)])
    co = map_data[x][y]
    if co == 'R' or co == 'G':
        co = 'R'
    visited[x][y] = True
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if map_data[nr][nc] == co or (map_data[nr][nc] == 'G' and co == 'R'):
                if not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

# 색약이 아닌 사람
visited1 = [[False] * n for _ in range(n)]  
color_yes = 0      
for row in range(n):
    for col in range(n):
        if not visited1[row][col]:
            color(row, col, arr, visited1)
            color_yes += 1 
# 색약
visited2 = [[False] * n for _ in range(n)]  
color_no = 0      
for row in range(n):
    for col in range(n):
        if not visited2[row][col]:
            colorless(row, col, arr, visited2)
            color_no += 1
print(color_yes, color_no)