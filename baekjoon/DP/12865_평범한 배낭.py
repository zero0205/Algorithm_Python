n, k = map(int, input().split())
items = [[0,0]]
for _ in range(n):
    items.append(list(map(int, input().split())))   # 무게, 가치
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1): # 물건 인덱스 (1~n)
    for j in range(1, k+1): # 무게 (1~k)
        w, v = items[i]
        if j < w:       # 무게가 현재 보고 있는 물건보다 작음
            dp[i][j] = dp[i-1][j]   # 물건 안 넣음
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])