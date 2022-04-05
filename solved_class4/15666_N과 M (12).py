# https://www.acmicpc.net/problem/15666

# from itertools import combinations_with_replacement

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()

# for el in list(sorted(set(combinations_with_replacement(arr, m)))):
#     for e in el:
#         print(e, end=' ')
#     print()
####################
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = []

def dfs(idx, cnt, m, ans):
    if cnt == m:
        res.append(tuple(ans))
        return
    for i in range(idx, n):
        ans.append(arr[i])
        dfs(i, cnt + 1, m, ans)
        ans.pop()

dfs(0, 0, m, [])

for el in sorted(list(set(res))):
    for e in el:
        print(e, end=' ')
    print()