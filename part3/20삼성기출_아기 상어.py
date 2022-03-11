# https://www.acmicpc.net/problem/16236

# import heapq

# # 공간의 크기 n 입력받기
# n = int(input())
# # 공간의 상태 입력받기
# map_data = []
# for _ in range(n):
#     map_data.append(list(map(int, input().split())))
    
# # 물고기들의 크기, 위치 파악
# fishes = []
# for i in range(n):
#     for j in range(n):
#         if 0 < map_data[i][j] <= 6:  # 물고기 위치
#             fishes.append((map_data[i][j], i, j))   # (크기, 행, 열)
#         elif map_data[i][j] == 9:   # 아기 상어 위치
#             baby_shark = (2, i, j)  # (크기, 행, 열)
            
# # 물고기들 크기 순으로 정렬
# fishes.sort()

# # 물고기 중에 먹을 수 있는 물고기들 뽑아내기
# sec = 0

# while fishes:
#     min_row = int(1e9)
#     min_col = int(1e9)
#     min_sec = int(1e9)
#     for fish in fishes:
#         size, row, col = fish
#         if size >= baby_shark[0]: # 물고기의 크기가 아기 상어보다 크거나 같다면 못 먹음
#             break
#         # 아기 상어로부터 가장 가까운 거리에 있는지 확인
#         if min_sec > (abs(row - baby_shark[1]) + abs(col - baby_shark[2])):
#             min_row = row
#             min_col = col
#             min_sec = abs(row - baby_shark[1]) + abs(col - baby_shark[2])
            
### 답지 ### 
from collections import deque
INF = 1e9   # 무한을 의미하는 값으로 10억을 설정

# 맵의 크기 N을 입력받기
n = int(input())           

# 전체 모든 칸에 대한 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
                 
# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0
            
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리만' 계산하는 BFS 함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist   # 먹을 물고기의 위치와 최단 거리
    
result = 0  # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0
### test case ###
# 3
# 0 0 0
# 0 0 0
# 0 9 0

# 3
# 0 0 1
# 0 0 0
# 0 9 0

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4