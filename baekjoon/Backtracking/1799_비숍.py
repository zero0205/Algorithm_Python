import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

rb_diag = {k: 0 for k in range(-n+1, n)}


def check_possible(diag):   # 앞으로 몇 개 더 놓을 수 있는지?
    res = 0
    for d in range(diag, 2*n-1):
        for x in range(d+1):
            y = d-x
            if 0 <= x < n and 0 <= y < n and board[x][y] and rb_diag[x-y] == 0:
                res += 1
                break
    return res


def bt(lb_diag, bishops):   # 백트래킹
    global ans
    if lb_diag == n*2-1:
        ans = max(ans, bishops)
        return
    possible = check_possible(lb_diag)
    # 앞으로 가능한 개수를 모두 놓아도 현재 ans보다 적을 때 return
    if possible+bishops <= ans:
        return
    for x in range(lb_diag+1):  # 현재 대각선에서 놓을 수 있는 칸들
        y = lb_diag-x
        if 0 <= x < n and 0 <= y < n and board[x][y] and rb_diag[x-y] == 0:
            rb_diag[x-y] = 1
            bt(lb_diag+1, bishops+1)
            rb_diag[x-y] = 0
    bt(lb_diag+1, bishops)


bt(0, 0)
print(ans)
