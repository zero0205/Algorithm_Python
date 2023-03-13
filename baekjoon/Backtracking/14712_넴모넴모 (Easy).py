n, m = map(int, input().split())
arr = [[False for _ in range(m+1)] for _ in range(n+1)]
ans = 0

def dfs(r,c):
    global ans
    if r == n + 1 and c == 1:
        ans += 1
        return
    if c == m:
        nr = r + 1
        nc = 1
    else:
        nr = r
        nc = c + 1
    # 이번 칸에 넴모를 놔도 2X2가 되지 않는 경우 넴모 놓기
    if not (arr[r-1][c-1] and arr[r-1][c] and arr[r][c-1]): 
        arr[r][c] = True
        dfs(nr, nc)
        arr[r][c] = False
    # 이번 칸에 넴모 안 놓고 지나가기
    dfs(nr, nc)
        
dfs(1, 1)
print(ans)