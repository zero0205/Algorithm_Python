import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if board[i][j] == '1':    # 뒷면
            # 뒤집기
            for r in range(i+1):
                for c in range(j+1):
                    board[r][c] = ('0' if board[r][c] == '1' else '1')
            ans += 1
print(ans)
