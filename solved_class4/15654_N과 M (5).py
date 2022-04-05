# https://www.acmicpc.net/problem/15654

# from itertools import permutations

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# for el in list(permutations(sorted(arr), m)):
#     for e in el:
#         print(e, end=" ")
#     print()
    
########################################
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(cnt, ans):
    if cnt == m:
        for a in ans:
            print(a, end=' ')
        print()
        return
    for i in range(0, n):
        if arr[i] not in ans:
            ans.append(arr[i])
            dfs(cnt + 1, ans)
            ans.pop()

dfs(0, [])