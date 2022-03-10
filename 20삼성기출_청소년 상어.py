# # https://www.acmicpc.net/problem/19236

# from copy import deepcopy

# # 위쪽 방향부터 반시계 방향으로 45도씩(0 ~ 7)
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, -1, -1, -1, 0, 1, 1, 1]

# # 물고기 이동 함수
# def fish_move(map_data, num, x, y, dir):    # 맵데이터, 물고기번호, 위치, 방향
#     # 상어가 있거나 범위 벗어나면 이동 불가
#     for i in range(8):
#         nx = x + dx[(dir + i) % 8]
#         ny = y + dy[(dir + i) % 8]   
#         # 범위를 벗어나는 경우
#         if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
#             continue
#         # 상어가 있는 경우
#         elif map_data[nx][ny][0] == -1:
#             continue
#         # 빈칸인 경우
#         elif map_data[nx][ny][0] == 0:
#             map_data[nx][ny] = (num, i + 1) # 빈칸으로 물고기 이동
#             map_data[x][y] = (0, 0) # 원래 있던 칸은 빈 칸으로 처리
#             break
#         # 다른 물고기와 위치를 바꾸는 경우
#         else:
#             # 물고기들 위치 테이블 갱신
#             fish_location[num] = (nx, ny)
#             fish_location[map_data[nx][ny][0]] = (x, y)
#             # 맵 데이터 갱신
#             map_data[x][y] = map_data[nx][ny]   
#             map_data[nx][ny] = (num, i + 1)

#             break
        
# # 전체 물고기 이동 함수
# def fishes_move(map_data):
#     # 1번부터 순차적으로 이동
#     for i in range(1, 17):
#         x = fish_location[i][0]
#         y = fish_location[i][1]
#         fish_move(map_data, i, x, y, map_data[x][y][1])

# # 상어 이동 함수
# def shark_move(map_data, x, y, dir):
#     copy_map = deepcopy(map_data)

#     nx = x + dx[dir]
#     ny = y + dy[dir]
#     # 범위를 벗어나는 경우
#     if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
#         return
#     # 빈칸인 경우
#     elif copy_map[nx][ny][0] == 0:
#         return
#     # 물고기 먹음
#     else:
#         result[nx][ny] = max(result[x][y] + copy_map[nx][ny][0], result[nx][ny]) # 결과 테이블 갱신
#         copy_map[x][y] = (0, 0)   # 상어 있던 자리 빈칸 됨
#         copy_map[nx][ny] = (-1, copy_map[nx][ny][1])    # 먹은 물고기의 방향을 가짐
#         # 물고기들 전체 이동
#         fishes_move(copy_map)
#         shark_move(copy_map, nx, ny, copy_map[nx][ny][1])
        
# # 상어의 현재 위치, 방향
# shark_location = (0, 0)
# shark_dir = 0
# # 최댓값 결과 저장할 테이블
# result = [[0] * 4 for _ in range(4)]

# # 번호별 물고기 위치 저장 테이블
# fish_location = [(0,0) for _ in range(17)]
      
# # 맵 데이터 입력받기
# map_data = []
# for i in range(4):
#     a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
#     map_data.append([(a1,b1 -1), (a2,b2 -1), (a3, b3 -1), (a4, b4 -1)])
#     # 물고기 번호별 위치 저장
#     fish_location[a1] = (i, 0)
#     fish_location[a2] = (i, 1)
#     fish_location[a3] = (i, 2)
#     fish_location[a4] = (i, 3)
    
# # # 맵 데이터 출력
# # for i in range(4):
# #     for j in range(4):
# #         print(f"({map_data[i][j][0]}, {map_data[i][j][1]})", end=' ')
# #     print()
    
# # 상어 입장
# shark_dir = map_data[0][0][1]
# result[0][0] = map_data[0][0][0]
# map_data[0][0] = (-1, shark_dir)    # 물고기 번호 -1이 상어

# # 물고기 첫번째 이동
# fishes_move(map_data)

# # 상어 이동 시작
# shark_move(map_data, 0, 0, shark_dir)

# # result 테이블에서 최댓값 출력
# answer = 0
# for r in range(4):
#     for c in range(4):
#         answer = max(answer, result[r][c])
# print(answer)

# # result 테이블 출력
# for i in range(4):
#     for j in range(4):
#         print(result[i][j], end=' ')
#     print()
    
####### 답지 ######
import copy

# 4 X 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향을 담는 테이블
array= [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] -1]
        
# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

result = 0  # 최종 결과

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
                
# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)    # 리스트를 통째로 복사
    
    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1 # 물고기를 먹었으므로 번호 값을 -1로 변환
    
    move_all_fishes(array, now_x, now_y)    # 전체 물고기 이동시키기
    
    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
        
# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)