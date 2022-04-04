# https://www.acmicpc.net/problem/15650

# from itertools import combinations

# n, m = map(int, input().split())
# lst = list(combinations(range(1, n + 1), m))

# for i in lst:
#     for j in i:
#         print(j, end=' ')
#     print()

######################

n, m = map(int, input().split())

def dfs(arr, v):
    if len(arr) == m:
        for i in arr:
            print(i, end=" ")
        print()
        return
    for j in range(v + 1, n + 1):
        arr.append(j)
        dfs(arr, j)
        arr.pop()
        
for start in range(1, n - m + 2):
    dfs([start], start)