from heapq import heappop, heappush

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

idx = 1

while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]

    losts = [[int(1e9)]*n for _ in range(n)]
    losts[0][0] = board[0][0]

    q = [(board[0][0], 0, 0)]
    while q:
        cnt, x, y = heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and losts[nx][ny] > cnt+board[nx][ny]:
                heappush(q, (cnt+board[nx][ny], nx, ny))
                losts[nx][ny] = losts[x][y]+board[nx][ny]
    print(f"Problem {idx}: {losts[n-1][n-1]}")
    idx += 1
