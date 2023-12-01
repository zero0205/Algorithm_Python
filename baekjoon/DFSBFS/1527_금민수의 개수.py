a, b = map(int, input().split())
ans = 0


def dfs(num):
    global ans
    if num > b:
        return
    if num >= a:
        ans += 1
    dfs(num*10 + 4)
    dfs(num*10 + 7)


dfs(0)
print(ans)
