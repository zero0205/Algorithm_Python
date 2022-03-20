# https://www.acmicpc.net/problem/1074/

# n, r, c = map(int, input().split())
# num = 0
# def dfs(x, y, n):
#     global num, arr, r, c
#     if n == 2:
#        for i in range(2):
#            for j in range(2):
#                if (x + i) == r and (y + j) == c:
#                    print(num)
#                    return
#                num += 1
#     else:
#         dfs(x, y, n // 2)
#         dfs(x, y + n // 2, n // 2)
#         dfs(x + n // 2, y, n // 2)
#         dfs(x + n // 2, y + n // 2, n // 2)
#     return

# dfs(0, 0, 2**n)