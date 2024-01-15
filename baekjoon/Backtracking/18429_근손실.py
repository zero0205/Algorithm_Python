n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = [False] * n
ans = 0


def bt(weight, used):
    global ans
    if weight < 500:
        return
    if used == n:
        ans += 1
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bt(weight+a[i]-k, used+1)
            visited[i] = False


bt(500, 0)
print(ans)
