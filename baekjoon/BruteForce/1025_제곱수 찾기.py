from math import sqrt

n, m = map(int, input().split())
board = [input() for _ in range(n)]

ans = -1

for r in range(n):  # 행
    for c in range(m):  # 열
        for i in range(-n+1, n):    # 행의 공차
            for j in range(-m+1, m):    # 열의 공차
                if i == 0 and j == 0:
                    if float.is_integer(sqrt(int(board[r][c]))):
                        ans = max(ans, int(board[r][c]))
                else:
                    rr, cc = r, c
                    tmp = ''
                    while True:
                        if 0 <= rr < n and 0 <= cc < m:
                            tmp += board[rr][cc]
                            if float.is_integer(sqrt(int(tmp))):
                                ans = max(ans, int(tmp))
                            rr += i
                            cc += j
                        else:
                            break

print(ans)
