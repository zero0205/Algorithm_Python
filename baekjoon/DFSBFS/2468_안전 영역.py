# https://www.acmicpc.net/problem/2468

from collections import deque
from copy import deepcopy


n = int(input())
# 지역 높이 정보 입력받기
input_data = []
max_h = 0
for _ in range(n):
    row = list(map(int, input().split()))
    max_h = max(max_h, max(row))
    input_data.append(row)
    
def bfs(x, y, height, map_data):
    q = deque([(x, y)])
    map_data[x][y] = -1   # 방문 처리
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map_data[nx][ny] > height:
                    q.append((nx, ny))
                    map_data[nx][ny] = -1 # 방문처리
                    
answer = 0
for h in range(0, max_h + 1):
    res = 0
    safezone = 0
    new_data = deepcopy(input_data)
    # 높이가 h일 때의 안전구역의 개수 구하기
    for r in range(n):
        for c in range(n):
            if new_data[r][c] > h:
                bfs(r,c,h,new_data)
                res += 1
    answer = max(answer, res)
    
print(answer)