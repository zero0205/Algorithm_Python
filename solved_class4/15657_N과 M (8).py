# https://www.acmicpc.net/problem/15657

# from itertools import combinations_with_replacement

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# for el in list(combinations_with_replacement(sorted(arr), m)):
#     for e in el:
#         print(e, end=" ")
#     print()
    
###########################################
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(idx, cnt, ans):
    if cnt == m:
        for a in ans:
            print(a, end=' ')
        print()
        return
    for i in range(idx, n):
        ans.append(arr[i])
        dfs(i, cnt + 1, ans)
        ans.pop()
        
dfs(0, 0, [])