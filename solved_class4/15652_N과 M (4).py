# https://www.acmicpc.net/problem/15652

# from itertools import combinations_with_replacement

# n, m = map(int, input().split())

# lst = list(combinations_with_replacement(range(1, n + 1), m))

# for el in lst:
#     for e in el:
#         print(e, end=" ")
#     print()
##########################################
n, m = map(int, input().split())

def dfs(v, cnt, arr):
    if cnt == m:
        for el in arr:
            print(el, end=' ')
        print()
        return
    for i in range(v, n + 1):
        arr.append(i)
        dfs(i, cnt + 1, arr)
        arr.pop()
dfs(1, 0, [])    