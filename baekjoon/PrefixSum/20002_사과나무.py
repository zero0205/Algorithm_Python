n = int(input())
profits = [list(map(int, input().split())) for _ in range(n)]

accum = [[0]*(n+1) for _ in range(n+1)]  # 누적합
for i in range(1, n+1):
    for j in range(1, n+1):
        accum[i][j] = accum[i-1][j]+accum[i][j-1] - \
            accum[i-1][j-1]+profits[i-1][j-1]

ans = -int(1e9)
for i in range(1, n+1):  # 행
    for j in range(1, n+1):  # 열
        for k in range(1, min(i, j)+1):  # K x K 정사각형 한 변 길이 K
            p = accum[i][j]-accum[i-k][j]-accum[i][j-k]+accum[i-k][j-k]
            if p > ans:
                ans = p
print(ans)
