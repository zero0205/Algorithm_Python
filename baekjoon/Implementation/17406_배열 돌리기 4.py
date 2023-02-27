# from itertools import permutations
# from copy import deepcopy

# n, m, k = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# def rotate(p_arr, arr_data):
#     for op in p_arr: # p_arr은 연산들 순서 저장 배열
#         r, c, s = op[0] - 1, op[1] - 1, op[2]
#         for cnt in range(s):    # s번의 정사각형 회전
#             top_r, top_c = r-s+cnt, c-s+cnt   # 왼위
#             bottom_r, bottom_c = r+s-cnt, c+s-cnt   # 오른아래
#             # a d
#             # b c
#             a,b,c,d = arr_data[top_r][top_c], arr_data[bottom_r][top_c], arr_data[bottom_r][bottom_c], arr_data[top_r][bottom_c]
#             # 윗줄
#             for col in range(bottom_c, top_c, -1):
#                 arr_data[top_r][col] = arr_data[top_r][col-1] # 윗줄
#             arr_data[top_r][top_c+1] = a   # 윗줄
#             # 아랫줄
#             for col in range(top_c, bottom_c):
#                 arr_data[bottom_r][col] = arr_data[bottom_r][col+1] # 아랫줄
#             arr_data[bottom_r][bottom_c-1] = c   # 아랫줄
#             # 왼줄
#             for row in range(top_r, bottom_r):
#                 arr_data[row][top_c] = arr_data[row+1][top_c] # 왼줄
#             arr_data[bottom_r-1][top_c] = b   # 왼줄
#             # 오른줄
#             for row in range(bottom_r, top_r, -1):
#                 arr_data[row][bottom_c] = arr_data[row-1][bottom_c] # 오른줄
#             arr_data[top_r+1][bottom_c] = d   # 오른줄


# cmd = []
# for _ in range(k):
#     cmd.append(list(map(int, input().split())))

# ans = 5001
# for p_arr in permutations(cmd, len(cmd)):   # 가능한 순열 모두 만들기
#     new_arr = deepcopy(arr)
#     rotate(p_arr, new_arr)
#     for r in new_arr:
#         ans = min(ans, sum(r))

# print(ans)

##############################
from collections import deque
from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
def rotate(r, c, s, arr_data):
    for cnt in range(s):    # s번의 정사각형 회전
        top_r, top_c = r-s+cnt, c-s+cnt   # 왼위
        bottom_r, bottom_c = r+s-cnt, c+s-cnt   # 오른아래
         
        q = deque([])
        # 왼줄
        for i in range(top_r, bottom_r):
            q.append(arr_data[i][top_c])
        # 아랫줄
        for i in range(top_c, bottom_c):
            q.append(arr_data[bottom_r][i])
        # 오른줄
        for i in range(bottom_r, top_r, -1):
            q.append(arr_data[i][bottom_c])
        # 윗줄
        for i in range(bottom_c, top_c, -1):
            q.append(arr_data[top_r][i])
        
        q.rotate(-1)
        
        # 왼줄
        for i in range(top_r, bottom_r):
            arr_data[i][top_c] = q.popleft()
        # 아랫줄
        for i in range(top_c, bottom_c):
            arr_data[bottom_r][i] = q.popleft()
        # 오른줄
        for i in range(bottom_r, top_r, -1):
            arr_data[i][bottom_c] = q.popleft()
        # 윗줄
        for i in range(bottom_c, top_c, -1):
            arr_data[top_r][i] = q.popleft()

cmd = []
for _ in range(k):
    cmd.append(list(map(int, input().split())))       

ans = 5001
for p in permutations(cmd, len(cmd)):
    new_arr = deepcopy(arr)
    for op in p:    # p는 연산 순서 저장된 배열
        rotate(op[0]-1, op[1]-1, op[2], new_arr)
    for r in new_arr:
        ans = min(ans, sum(r))

print(ans)