# from copy import deepcopy
# from itertools import combinations

# # n 입력받기
# n = int(input())
# # 복도 정보 입력받기
# map_data = []
# for i in range(n):
#     map_data.append(list(input().split()))

# # 빈 칸 위치 파악
# empty_space = []
# for r in range(n):
#     for c in range(n):
#         if map_data[r][c] == 'X':
#             empty_space.append((r, c))

# selected = combinations(empty_space, 3)

# is_safe = False

# def go_straight(r, c, map_data, dir_idx):
#     dir = [(-1,0),(1,0),(0,-1),(0,1)]
#     nr = r + dir[dir_idx][0]
#     nc = c + dir[dir_idx][1]
#     # 벽 또는 방해물에 닿을 때까지 학생 못 봄
#     if nr < 0 or nr >=len(map_data) or nc < 0 or nc >= len(map_data) or map_data[nr][nc] == 'O':
#         return True
#     if map_data[nr][nc] == 'S': # 학생 잡음
#         return False
#     go_straight(nr, nc, map_data, dir_idx)

# for d1, d2, d3 in selected:
#     new_map = deepcopy(map_data)
#     # 방해물 설치
#     new_map[d1[0]][d1[1]] = 'O' 
#     new_map[d2[0]][d2[1]] = 'O' 
#     new_map[d3[0]][d3[1]] = 'O' 

#     for r in range(n):
#         for c in range(n):
#             if new_map[r][c] == 'T':
#                 for i in range(4):
#                     if not go_straight(r,c,new_map,i): # 잡힘 -> 더이상 확인할 필요 X
#                         is_safe = False
#                         break       
#             if not is_safe:
#                 break
#         if not is_safe:
#                 break
#         else:
#             is_safe = True
#     if is_safe:
#         print("YES")
#         break

# if not is_safe:
#     print("NO")

###################
from copy import deepcopy
from itertools import combinations

# n 입력받기
n = int(input())
# 복도 정보 입력받기
map_data = []   # 복도 정보 저장
teachers = []   # 선생님들 위치 저장
spaces = []     # 빈 칸들 위치 저장

for i in range(n):
    map_data.append(list(input().split()))
    # 선생님들 위치 파악
    for j in range(n):
        if map_data[i][j] == 'T':
            teachers.append((i,j))
    # 빈 칸 위치 파악
    for j in range(n):
        if map_data[i][j] == 'X':
            spaces.append((i,j))


def go_straight(r, c, map_data, dir_idx):
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    nr = r + dir[dir_idx][0]
    nc = c + dir[dir_idx][1]
    # 벽 또는 방해물에 닿을 때까지 학생 못 봄
    if nr < 0 or nr >=len(map_data) or nc < 0 or nc >= len(map_data) or map_data[nr][nc] == 'O':
        return False
    if map_data[nr][nc] == 'S': # 학생 잡음
        return True

def check():
    for x, y in teachers:
        for i in range(4):
            if go_straight(x,y,map_data, i):
                return True

is_safe = False

for d1, d2, d3 in combinations(spaces, 3):
    # 방해물 설치
    map_data[d1[0]][d1[1]] = 'O' 
    map_data[d2[0]][d2[1]] = 'O' 
    map_data[d3[0]][d3[1]] = 'O' 

    if not check(): # 학생 발견 못 함
        is_safe = True
        break

    # 방해물 다시 제거
    map_data[d1[0]][d1[1]] = 'X' 
    map_data[d2[0]][d2[1]] = 'X' 
    map_data[d3[0]][d3[1]] = 'X' 

if is_safe:
    print("YES")
else:
    print("NO")