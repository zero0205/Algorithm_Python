# https://www.acmicpc.net/problem/2448

n = int(input())    # n은 항상 3*2^k

arr = [[' '] * 2 * n for _ in range(n)]

def star(x, y, n):
    if n == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = arr[x+1][y+1] = '*'
        for i in range(-2, 3):
            arr[x+2][y+i] = '*'
    else:
        next = n // 2
        star(x, y, next)
        star(x + next, y - next, next)
        star(x + next, y + next, next)
star(0, n-1, n)

for r in arr:
    print("".join(r))