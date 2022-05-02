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

def bfs(): 
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True    # 외부 공기

    # 외부 공기 판단
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위 안 벗어남
                if paper[nx][ny] == 0 and not visited[nx][ny]:  # 외부 공기
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else:   # 치즈면 +1 해주고 감 (외부 공기와 맞닿은 면이 있을 때마다 1 증가)
                    if not visited[nx][ny]:
                        paper[nx][ny] += 1
ans = 0
while True:
    bfs()
    melt = False
    
    for r in range(n):
        for c in range(m):
            if paper[r][c] >= 3:    # 외부 공기와 2면 이상 맞닿은 치즈 = 이번에 녹음
                paper[r][c] = 0
                melt = True
            elif paper[r][c] == 2:
                paper[r][c] = 1
    if melt:
        ans += 1
    else:
        break
    
print(ans)