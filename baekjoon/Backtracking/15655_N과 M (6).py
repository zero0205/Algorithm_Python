# from itertools import combinations

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))

# for comb in combinations(arr, m):
#     print(*comb)
####################################################
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

lst = []

def dfs(idx):
    if idx > n:
        return
    if len(lst) == m:
        print(*lst)
        return
    for i in range(idx, n):
        lst.append(arr[i])
        dfs(i+1)
        lst.pop()
        
dfs(0)