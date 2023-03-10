n, m = map(int, input().split())

arr = []
def dfs(num):
    if num > n:
        return
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)