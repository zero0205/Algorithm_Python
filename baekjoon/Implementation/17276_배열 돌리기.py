from collections import deque

def rotation(x, n, d):
    diagnol1 = deque([])
    diagnol2 = deque([])
    center_row = deque([])
    center_col = deque([])
    for i in range(n):
        if i != n // 2:
            diagnol1.append(x[i][i])        # 왼위->오른아래 대각선
            diagnol2.append(x[i][n-1-i])    # 오른위->왼아래 대각선
            center_row.append(x[n//2][i])   # 가운데 행
            center_col.append(x[i][n//2])   # 가운데 열
    if d > 0:       # 시계 방향
        for i in range(n):
            if i == n//2:
                continue
            x[i][i] = center_row.popleft()      # 왼위->오른아래 대각선
            x[i][n-1-i] = center_col.popleft()  # 오른위->왼아래 대각선
            x[i][n//2] = diagnol1.popleft()     # 가운데 열
            x[n//2][i] = diagnol2.pop()         # 가운데 행
    else:           # 반시계 방향
        for i in range(n):
            if i == n//2:
                continue
            x[i][i] = center_col.popleft()      # 왼위->오른아래 대각선
            x[i][n-1-i] = center_row.pop()      # 오른위->왼아래 대각선
            x[n//2][i] = diagnol1.popleft()     # 가운데 행
            x[i][n//2] = diagnol2.popleft()     # 가운데 열
    return x

for _ in range(int(input())):
    n, d = map(int, input().split())
    x = []
    for _ in range(n):
        x.append(list(map(int, input().split())))
    for _ in range(abs(d) // 45):
        rotation(x, n, d)
    # 돌아간 x 출력
    for i in range(n):
        print(*x[i])