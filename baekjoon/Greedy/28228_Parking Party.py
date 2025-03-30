import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parking_lot = [list(input()) for _ in range(n)]

# 위쪽
for c in range(m):
    r = 0
    while r < n and parking_lot[r][c] != "o":
        parking_lot[r][c] = "-"
        r += 1
# 아래쪽
for c in range(m):
    r = n-1
    while r >= 0 and parking_lot[r][c] != "o":
        parking_lot[r][c] = "-"
        r -= 1
# 왼쪽
for r in range(n):
    c = 0
    while c < m and parking_lot[r][c] != "o":
        parking_lot[r][c] = "-"
        c += 1
# 오른쪽
for r in range(n):
    c = m-1
    while c >= 0 and parking_lot[r][c] != "o":
        parking_lot[r][c] = "-"
        c -= 1

answer = 0
for i in range(n):
    for j in range(m):
        if parking_lot[i][j] == "-":
            answer += 1
print(answer)
