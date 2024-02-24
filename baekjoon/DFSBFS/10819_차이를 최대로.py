n = int(input())
a_lst = list(map(int, input().split()))

ans = -1000
visited = [False]*n


def dfs(depth, total, prev):
    global ans
    if depth == n:
        ans = max(total, ans)
        return
    for i in range(n):
        if not visited[i]:
            tmp = 0
            if depth != 0:
                tmp = abs(prev-a_lst[i])
            visited[i] = True
            dfs(depth+1, total+tmp, a_lst[i])
            visited[i] = False


dfs(0, 0, -1)
print(ans)
