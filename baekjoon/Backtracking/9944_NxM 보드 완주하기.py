dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = 0, 0
blank = 0
ans = int(1e9)

def backtracking(x, y, cnt, move):
    global n, m, blank, ans
    if move >= ans:    # 최소 이동 횟수보다 커지면 더 볼 필요 X
        return
    if cnt == blank:  # 모든 빈 칸 방문 완료
        ans = min(ans, move)
        return
    path = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':    # 이동
            board[nx][ny] = '*' # 방문 처리
            path.append((nx, ny))
            nx += dx[i]
            ny += dy[i]
        if path:    # 움직임이 있었음
            backtracking(nx-dx[i], ny-dy[i], cnt+len(path), move+1)
        for i in range(len(path)):   # 방문 처리했던 칸들 다시 원상복구
            r, c = path.pop()
            board[r][c] = '.'
tc = 1    
while True:
    try:
        n, m = map(int, input().split())
        board = []
        blank = 0   # 빈 칸 개수
        for i in range(n):
            board.append(list(input())) # *은 장애물, .은 빈 칸
            for j in range(m):  # 빈 칸 개수 세기
                if board[i][j] == '.':
                    blank += 1

        ans = int(1e9)
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    board[i][j] = '*'   # 방문 처리
                    backtracking(i, j, 1, 0)
                    board[i][j] = '.'
        print("Case {}: {}".format(tc, ans if ans != int(1e9) else -1))
        tc += 1
    except:
        break