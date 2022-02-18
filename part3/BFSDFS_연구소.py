# https://www.acmicpc.net/problem/14502

from collections import deque
from copy import deepcopy
from itertools import combinations

# n, m 입력받기
n, m = map(int, input().split())
# 지도 입력받기
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))

# 벽 3개 세워주기
def build_wall(graph, wall_location):
    wall1, wall2, wall3 = wall_location # 벽은 꼭 3개 세움
    graph[wall1[0]][wall1[1]] = 1
    graph[wall2[0]][wall2[1]] = 1
    graph[wall3[0]][wall3[1]] = 1
    return graph

# 상하좌우
dir = [(-1,0),(1,0),(0,-1),(0,1)]

# BFS
def bfs(graph, row, col):
    que = deque([(row, col)])
    while que:
        r, c = que.popleft()
        for j in range(4):  # 상하좌우로 탐색
            nr = r + dir[j][0]
            nc = c + dir[j][1]
            if nr < 0 or nr >= len(graph) or nc < 0 or nc >= len(graph[0]): # 범위를 벗어남
                continue
            if graph[nr][nc] == 0:
                que.append((nr, nc))
                graph[nr][nc] = 2   # 바이러스 퍼짐

# 안전 구역 크기 파악
def check_safe(graph, n, m):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                cnt +=1
    return cnt

# 빈 칸들 위치 파악
empty = []
for r in range(n):
    for c in range(m):
        if map_data[r][c] == 0:
            empty.append((r,c))

selected = list(combinations(empty, 3))
safe = -1
for el in selected:
    new_map = deepcopy(map_data)
    new_map = build_wall(new_map, el)
    # 바이러스 퍼져나가는거 체크
    for row in range(n):
        for col in range(m):
            if new_map[row][col] == 2:
                bfs(new_map, row, col)
    # 안전구역 체크
    safe = max(safe, check_safe(new_map, n, m))

print(safe)