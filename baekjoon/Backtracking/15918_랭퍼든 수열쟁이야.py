n, x, y = map(int, input().split())
location = [[] for _ in range(n+1)]
ans = 0
visited = [False]*(2*n)
visited[x-1] = True
visited[y-1] = True


def bt(num):
    global ans
    if num > n:
        ans += 1
        return
    if num == (y-x-1):
        bt(num+1)
        return
    for i in range(2*n-num-1):
        if not visited[i] and not visited[i+num+1]:
            visited[i] = True
            visited[i+num+1] = True
            bt(num+1)
            visited[i] = False
            visited[i+num+1] = False


bt(1)
print(ans)
