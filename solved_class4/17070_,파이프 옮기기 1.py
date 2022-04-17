# https://www.acmicpc.net/problem/17070

########## BFS(시간 초과) #############
# from collections import deque

# n = int(input())
# home = [list(map(int, input().split())) for _ in range(n)]

# # 다음에 이동 가능한 위치 리스트 리턴
# def move(x1, y1, x2, y2):
#     ans = []
#     # 가로로 놓여있는 경우
#     if x1 == x2:
#         # 오른쪽으로 못 가는 경우
#         if y2 + 1 >= n or home[x2][y2 + 1] == 1: 
#             return []
#         # 오른쪽으로 밀기
#         ans.append((x2, y2, x2, y2 + 1))
#         # 대각선
#         if x2 + 1 < n and home[x2 + 1][y2] == 0 and home[x2 + 1][y2 + 1] == 0:
#             ans.append((x2, y2, x2 + 1, y2 + 1))
#         return ans
#     # 세로로 놓여있는 경우
#     elif y1 == y2:
#         # 아래쪽으로 못 가는 경우
#         if x2 + 1 >= n or home[x2 + 1][y2] == 1: 
#             return []
#         # 아래쪽으로 밀기
#         ans.append((2, y2, x2 + 1, y2))
#         # 대각선
#         if y2 + 1 < n and home[x2][y2 + 1] == 0 and home[x2 + 1][y2 + 1] == 0:
#             ans.append((x2, y2, x2 + 1, y2 + 1))
#         return ans
#     # 대각선으로 놓여있는 경우
#     else:
#         # 오른쪽으로 밀기
#         if y2 + 1 < n and home[x2][y2 + 1] == 0:    
#             ans.append((x2, y2, x2, y2 + 1))
#          # 아래쪽으로 밀기
#         if x2 + 1 < n and home[x2 + 1][y2] == 0:    
#             ans.append((x2, y2, x2 + 1, y2))
#         # 대각선
#         if x2 + 1 < n and y2 + 1 < n and home[x2 + 1][y2] == 0 and home[x2 + 1][y2 + 1] == 0 and home[x2][y2 + 1] == 0:
#             ans.append((x2, y2, x2 + 1, y2 + 1))
#         return ans
# q = deque([(0, 0, 0, 1)])
# ans = 0
# while q:
#     x1, y1, x2, y2 = q.popleft()
#     total_lst = move(x1, y1, x2, y2)
#     for nx1, ny1, nx2, ny2 in total_lst:
#         if nx2 == n - 1 and ny2 == n - 1:
#             ans += 1
#             continue
#         q.append((nx1, ny1, nx2, ny2))
        
# print(ans)

################ DP ####################
