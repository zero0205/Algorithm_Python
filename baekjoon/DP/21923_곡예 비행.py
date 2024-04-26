n, m = map(int, input().split())
scores = [[0]+list(map(int, input().split())) for _ in range(n)]

up = [[-int(1e9)]*(m+1) for _ in range(n+1)]    # 상승 비행 점수
down = [[-int(1e9)]*(m+1) for _ in range(n+1)]  # 하강 비행 점수
up[n-1][1] = scores[n-1][1]  # 출발점

# 상승
for j in range(1, m+1):
    for i in range(n-1, -1, -1):
        if i == n-1:    # 바닥
            if j == 1:
                continue
            up[i][j] = up[i][j-1]    # 앞
        else:
            up[i][j] = max(up[i][j-1], up[i+1][j])    # 앞, 위
        up[i][j] += scores[i][j]
# 하강
for j in range(1, m+1):
    for i in range(n):
        if j == 1:  # 출발 열
            down[i][j] = max(up[i][j], down[i-1][j])    # 상승->하강, 아래
        elif i == 0:      # 천장
            down[i][j] = max(up[i][j], down[i][j-1])    # 상승->하강, 앞
        else:
            down[i][j] = max(up[i][j], down[i][j-1],
                             down[i-1][j])  # 상승->하강, 앞, 아래
        down[i][j] += scores[i][j]
print(down[n-1][m])
