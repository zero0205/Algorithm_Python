# #### Bottom-Up ####
# import sys
# from unittest import result
# input = sys.stdin.readline

# # 다이나믹 프로그래밍
# def dp(r, c, tri, dp_table):
#     global n
#     for i in [0,1]:
#         nr = r + 1
#         nc = c + i
#         if nr >= n or nc < 0 or nc >= len(tri[nc]): # 범위를 벗어남
#             continue
#         # 새로운 값이 원래값보다 크다면 갱신
#         new_value = dp_table[r][c] + tri[nr][nc]
#         if new_value > dp_table[nr][nc]:
#             dp_table[nr][nc] = new_value

# # 삼각형의 크기 n 입력받기
# n = int(input())
# # 삼각형 입력받기
# tri = []
# for _ in range(n):
#     tri.append(list(map(int, input().split())))
# # dp_table 생성
# dp_table = [[0] * (i + 1) for i in range(n)]
# dp_table[0][0] = tri[0][0]
# for r in range(n):
#     for c in range(len(tri[r])):
#         dp(r,c,tri, dp_table)

# print(max(dp_table[-1]))

#### Top-down ####
import sys
input = sys.stdin.readline

# 삼각형의 크기 n 입력받기
n = int(input())
# 삼각형 입력받기
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
    
dp_table = [[0] * n for _ in range(n)]
def dp(r,c):
    if r == 0:  # 삼각형 꼭대기 제일 첫번째 값
        return tri[r][c]
    if dp_table[r][c] != 0: # 이미 계산했던 값
        return dp_table[r][c]
    # 본인 바로 위랑 왼쪽 위 보면 됨
    if c == r:  # 오른쪽 끝 -> 본인 왼쪽 위만 보면 됨
        dp_table[r][c] = tri[r][c] + dp(r-1, c-1)
    elif c == 0:  # 왼쪽 끝 -> 바로 위만 보면 됨
        dp_table[r][c] = tri[r][c] + dp(r-1, c)
    else:
        dp_table[r][c] = tri[r][c] + max(dp(r-1,c-1), dp(r-1,c))
    return dp_table[r][c]

res = 0
for j in range(n):
    res = max(res, dp(n-1, j))
print(res)