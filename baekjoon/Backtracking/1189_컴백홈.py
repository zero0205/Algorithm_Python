def bt(x, y, cnt):
    global ans

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if x == 0 and y == c-1 and cnt == k:
        ans += 1
        return

    if cnt > k:  # 거리가 k를 초과하면 더 이상 탐색하지 않음
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
            board[nx][ny] = 'V'
            bt(nx, ny, cnt+1)
            board[nx][ny] = '.'


r, c, k = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

ans = 0

board[r-1][0] = 'V'  # 출발점 방문 표시
bt(r-1, 0, 1)

print(ans)
