# https://www.acmicpc.net/problem/2638

# from copy import deepcopy
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(n)]
# def is_melt(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     c = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if paper[nx][ny] == 0:  # 외부 공기와 접촉한다면
#             c += 1
#     if c >= 2: 
#         return True # 녹을거임
#     else:
#         return False    # 안 녹아
    
# # 치즈들 위치 파악
# cheeze = []
# for r in range(n):
#     for c in range(m):
#         if paper[r][c] == 1:
#             cheeze.append((r, c))    # 행, 열, 시간
# cnt = 0 
# while cheeze:
#     cnt += 1
#     disappear = []
#     remain = []
#     for x, y in cheeze:
#         if is_melt(x, y):
#             disappear.append((x, y))
#             continue
#         else:
#             remain.append((x, y))
#     # 녹은 치즈들 처리
#     for x, y in disappear:
#         paper[x][y] = 0   
#     # 남은 치즈 cheeze 배열로
#     cheeze = deepcopy(remain)
    
# print(cnt)
#############################
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if paper[nx][ny] == 1:  # 치즈임
            