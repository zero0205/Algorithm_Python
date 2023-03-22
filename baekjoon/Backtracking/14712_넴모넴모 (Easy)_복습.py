n, m = map(int, input().split())
board = [[False] * (m+1) for _ in range(n+1)]
ans = 0
    
# (x, y)에 넴모를 올렸을 때 2X2가 만들어지는지?
def nemo(x, y):
    if board[x-1][y-1] and board[x-1][y] and board[x][y-1]:
        return True
    return False

def dfs(x, y):
    global ans
    if x == n + 1 and y == 1:   # 끝까지 도달
        ans += 1
        return
    if y == m:
        nx = x + 1
        ny = 1
    else:
        nx = x
        ny = y + 1
    # (x, y)에 네모 놓아도 2X2 안되는 경우 네모 놓음
    if not nemo(x, y):
        board[x][y] = True
        dfs(nx, ny)
        board[x][y] = False
    # (x, y)에 네모 안 놓음
    dfs(nx,ny)

dfs(1,1)
print(ans)