from heapq import heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    n = int(input())
    board = [input() for _ in range(n)]

    t = [[int(1e9)]*n for _ in range(n)]
    t[0][0] = 0
    t[0][1] = int(board[0][1])
    t[1][0] = int(board[1][0])

    hq = []
    heappush(hq, (t[0][1], 0, 1))
    heappush(hq, (t[1][0], 1, 0))
    while hq:
        cost, x, y = heappop(hq)
        if x == n-1 and y == n-1:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and t[nx][ny] > t[x][y] + int(board[nx][ny]):
                t[nx][ny] = t[x][y] + int(board[nx][ny])
                heappush(hq, (t[nx][ny], nx, ny))
    print(f"#{tc} {t[n-1][n-1]}")
