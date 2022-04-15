# https://www.acmicpc.net/problem/14502

from collections import deque
from copy import deepcopy
from itertools import combinations

n, m = map(int, input().split())
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safe = 0

def wall_construct(map_data, walls):
    # 벽 3개 설치
    for wall in walls:
        map_data[wall[0]][wall[1]] = 1
    return map_data

def spread(n, m, map_data):    
    q = deque([])
    # 바이러스들 위치 덱에 넣기
    for i in range(n):
        for j in range(m):
            if map_data[i][j] == 2:
               q.append((i, j)) 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]) and map_data[nx][ny] == 0:
                q.append((nx, ny))
                map_data[nx][ny] = 2
    return map_data
                
def chk_safe_area(n, m, map_data):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if map_data[i][j] == 0:
                cnt += 1
    return cnt

# 현재 빈 칸들 위치 파악
empty = []
for i in range(n):
    for j in range(m):
        if map_data[i][j] == 0:
            empty.append((i, j))

walls_lst = list(combinations(empty, 3))

# 설치 가능한 벽 경우의 수 다 해보기
for walls in walls_lst:
    cpy_map = deepcopy(map_data)
    cpy_map = wall_construct(cpy_map, walls)
    cpy_map = spread(n, m, cpy_map)
    max_safe = max(max_safe, chk_safe_area(n, m, cpy_map))

print(max_safe)