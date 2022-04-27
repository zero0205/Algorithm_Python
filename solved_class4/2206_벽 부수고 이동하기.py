# # https://www.acmicpc.net/problem/2206

# from collections import deque
# from copy import deepcopy
# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# input_data = [input() for _ in range(n)]
# map_data = [[0] * m for _ in range(n)]
# for r in range(n):
#     for c in range(m):
#         if input_data[r][c] == '0':
#             map_data[r][c] = 0
#         else:
#             map_data[r][c] = 1

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 벽 위치들 파악
# walls = [(0, 0)]    # 벽 아무것도 안 부셨을때 계산하려고 (0, 0)도 넣음
# for r in range(n):
#     for c in range(m):
#         if map_data[r][c] == 1:
#             walls.append((r, c))

# def bfs(map_data): # 맵데이터 인자로 받음
#     q = deque([(0, 0, 1)]) # 행, 열, 거리
#     visited = [[False]*m for _ in range(n)]
#     visited[0][0] = True    #시작점 방문처리
#     while q:
#         x, y, l = q.popleft()
#         if x == n-1 and y == m-1:
#             return l
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >=m:
#                 continue
#             if map_data[nx][ny] == 0 and not visited[nx][ny]:
#                 q.append((nx, ny, l + 1))
#                 visited[nx][ny] = True
#     return int(1e9)

# min_path = int(1e9)
# for wall in walls:
#     new_map = deepcopy(map_data)
#     new_map[wall[0]][wall[1]] = 0
#     min_path = min(min_path, bfs(new_map))

# if min_path < int(1e9):
#     print(min_path)
# else:
#     print(-1)
#######################################
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
input_data = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)]) # 행, 열, 벽 부쉈는지 여부
    # 3차원 행렬
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1    # 처음 시작점 (0, 0) 방문처리
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=m:   # 범위 벗어남
                continue     
            if input_data[nx][ny] == 0 and visited[nx][ny][w] == 0: # 아직 방문 안 한 빈칸
                visited[nx][ny][w] = visited[x][y][w] + 1
                q.append((nx, ny, w))
            elif input_data[nx][ny] == 1 and w == 0:    # 벽인데 아직 뚫을 기회 남음  
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
    return -1   # 다 돌았는데도 목표지점까지 못 감

print(bfs())