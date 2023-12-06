board = []
for i in range(10):
    board.append(list(map(int, input().split())))

confeti = [0] * 6
ans = 26


def chk(r, c, l):
    for i in range(r, r+l):
        for j in range(c, c+l):
            if board[i][j] != 1:
                return False
    return True


def bt(r, c, cnt):
    global ans
    if c >= 10:
        bt(r+1, 0, cnt)  # 다음 행으로 넘어가기
        return
    if r >= 10:
        ans = min(ans, cnt)  # 끝까지 탐색
        return
    if board[r][c] == 1:
        for l in range(1, 6):
            if confeti[l] == 5:  # 이미 lXl 종이 다 씀
                continue
            if r+l-1 >= 10 or c+l-1 >= 10:  # 종이 붙이면 범위 넘어감
                continue
            if chk(r, c, l):
                for i in range(r, r+l):
                    for j in range(c, c+l):
                        board[i][j] = -1    # 종이 붙임
                confeti[l] += 1
                bt(r, c+l, cnt+1)
                confeti[l] -= 1
                for i in range(r, r+l):
                    for j in range(c, c+l):
                        board[i][j] = 1     # 종이 다시 떼기
    else:
        bt(r, c+1, cnt)


bt(0, 0, 0)
print(ans if ans < 26 else -1)
