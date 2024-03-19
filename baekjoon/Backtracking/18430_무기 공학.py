n, m = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]

boomerang = [[(0, -1), (1, 0)], [(0, -1), (-1, 0)],
             [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]
visited = [[False]*m for _ in range(n)]
ans = 0


def bt(x, y, total):
    global ans
    if y >= m:
        x += 1
        y = 0
        if x >= n:
            ans = max(ans, total)
            return
    if not visited[x][y]:
        for a, b in boomerang:  # 4방향 부메랑 가능한지
            ax = x+a[0]
            ay = y+a[1]
            bx = x+b[0]
            by = y+b[1]
            if 0 <= ax < n and 0 <= ay < m and 0 <= bx < n and 0 <= by < m and not visited[ax][ay] and not visited[bx][by]:
                visited[ax][ay] = True
                visited[bx][by] = True
                visited[x][y] = True
                bt(x, y+1, total+woods[x][y] *
                    2+woods[ax][ay]+woods[bx][by])
                visited[ax][ay] = False
                visited[bx][by] = False
                visited[x][y] = False
    bt(x, y+1, total)   # 이 자리에 안 놓음


bt(0, 0, 0)
print(ans)
