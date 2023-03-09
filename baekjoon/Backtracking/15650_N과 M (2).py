n, m = map(int, input().split())
visited = [False] * 9

def comb(i, arr):
    if len(arr) == m:
        print(*arr)
        return
    for j in range(i, n+1):
        if not visited[j]:
            visited[j] = True
            comb(j, arr+[j])
            visited[j] = False

comb(1, [])