# https://www.acmicpc.net/problem/12851

######### 메모리 초과ㅠㅠ##########
# from collections import deque

# n, k = map(int, input().split())

# def bfs():
#     min_t = int(1e9)
#     ans = 0
#     q = deque([(n, 0)])    
#     while q:
#         now, cnt = q.popleft()
#         if now == k:    # 동생 찾음
#             min_t = cnt # 동생을 찾는 가장 빠른 시간
#             ans += 1
#             while True: # 가장 빠른 시간으로 찾는 방법의 수 세기
#                 now, cnt = q.popleft()
#                 if cnt > min_t:
#                     return (min_t, ans)
#                 if now == k:
#                     ans += 1
#         # X - 1로 이동
#         if (now - 1) >= 0:
#             q.append((now - 1, cnt + 1))
#         # X + 1로 이동
#         if (now + 1) <= 100000:
#             q.append((now + 1, cnt + 1))
#         # X * 2로 이동
#         if (now * 2) <= 100000:
#             q.append((now * 2, cnt + 1))

# ans1, ans2 = bfs()
# print(ans1)
# print(ans2)

############################
# import sys
# sys.setrecursionlimit(10 ** 6)
# n, k = map(int, input().split())

# min_t, ans = int(1e9), 0

# def dfs(x, cnt, visited):
#     global min_t, ans
#     if cnt > min_t: # 최소시간보다 크면 더이상 볼 필요 X
#         return
#     if x == k:
#         if min_t > cnt: # 새로운 최소시간
#             ans = 1
#             min_t = cnt
#             return
#         else:
#             min_t = cnt
#             ans += 1
#             return
#     # X - 1 방문
#     if not visited[x - 1] and 0 <= (x - 1) <= 100000:
#         visited[x - 1] = True
#         dfs(x - 1, cnt + 1, visited)
#         visited[x - 1] = False
#     # X + 1 방문
#     if not visited[x + 1] and 0 <= (x + 1) <= 100000:
#         visited[x + 1] = True
#         dfs(x + 1, cnt + 1, visited)
#         visited[x + 1] = False
#     # X * 2 방문
#     if not visited[x * 2] and 0 <= (x * 2) <= 100000:
#         visited[x * 2] = True
#         dfs(x * 2, cnt + 1, visited)
#         visited[x * 2] = False

# visited = [False] * 100001
# dfs(n, 0, visited)
# print(min_t)
# print(ans)

################################################
from collections import deque

n, k = map(int, input().split())

def bfs(n):
    q = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1
    
    while q:
        now = q.popleft()
        
        for i in [now - 1, now + 1, now * 2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1: # 첫 방문
                    visited[i][0] = visited[now][0] + 1
                    visited[i][1] = visited[now][1]
                    q.append(i)
                elif visited[i][0] == visited[now][0] + 1: # 첫 방문 아님 & 최단 경로임
                    visited[i][1] += visited[now][1]                   
                    
visited = [[-1, 0] for _ in range(100001)]  # 최소 시간,경로의 개수

bfs(n)
print(visited[k][0])
print(visited[k][1])