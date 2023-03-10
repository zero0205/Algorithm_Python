# from itertools import combinations_with_replacement

# n, m = map(int, input().split())
# for comb in combinations_with_replacement(range(1, n+1), m):
#     print(*comb)
#########################################
n, m = map(int, input().split())
lst = []

def dfs(i):
    if i > n:
        return
    if len(lst) == m:
        print(*lst)
        return
    for j in range(i, n+1):
        lst.append(j)
        dfs(j)
        lst.pop()
        
dfs(1)