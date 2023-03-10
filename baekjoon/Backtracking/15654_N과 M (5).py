# from itertools import combinations

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))

# for comb in combinations(arr, m):
#     print(*comb)
    
###########################################
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

lst = []
visited = [False] * (n+1)

def dfs(idx):
    if idx > n:
        return
    if len(lst) == m:
        print(*lst)
        return
    for i in range(n):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            dfs(i+1)
            lst.pop()
            visited[i] = False
        
dfs(0)