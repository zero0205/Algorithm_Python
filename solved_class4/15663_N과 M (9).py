# https://www.acmicpc.net/problem/15663

# from itertools import permutations

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr = sorted(arr)

# for el in list(sorted(set(permutations(arr, m)))):
#     for e in el:
#         print(e, end=' ')
#     print()

################################
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = []

def dfs(cnt, ans, visited):
    if cnt == m:
        res.append(tuple(ans))
        return
    for i in range(0, n):
        if not visited[i]:
            ans.append(arr[i])
            visited[i] = True
            dfs(cnt + 1, ans, visited)
            visited[i] = False
            ans.pop()
            
visited = [False] * n           
dfs(0, [], visited)

for el in list(sorted(set(res))):
    for e in el:
        print(e, end=' ')
    print()