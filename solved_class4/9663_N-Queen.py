# https://www.acmicpc.net/problem/9663

# from collections import deque

# def attack_possible(x1, y1, x2, y2):
#     if x1 == x2 or y1 == y2: # 같은 행 또는 열
#         return True
#     if abs(x1 - x2) == abs(y1 - y2): # 대각선
#         return True
#     return False

# n = int(input())
# ans = 0
# for i in range(n):  
#     q = deque([(0, i)])
#     while q:
#         x1, y1 = q.popleft()
#         if y1 == (n - 1):
#             ans += 1
#             continue
#         for x2 in range(x1 + 1, n):
#             for y2 in range(n):
#                 if not attack_possible(x1, y1, x2, y2):
#                     q.append((x2, y2))

# print(ans)

############################
import sys
sys.setrecursionlimit(10000)

n = int(input())
row = [0] * n   # 인덱스번째 행에는 원소값의 열에 퀸이 있음
ans = 0

def attack_possible(x):
    for i in range(x):  # 행
        if row[i] == row[x]:   # 같은 열
            return True
        if abs(row[i] - row[x]) == (x - i):  # 대각선
            return True
    return False
            
def dfs(x):
    global ans
    if x == n:
        ans += 1
        return 
    else:
        for i in range(n):
            row[x] = i
            if not attack_possible(x):
                dfs(x + 1)

dfs(0)
print(ans)