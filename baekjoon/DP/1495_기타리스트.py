n, s, m = map(int, input().split())
v = [0]+list(map(int, input().split()))

dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][s] = True
ans = -1
for i in range(1, n+1):
    for j in range(m+1):
        if j-v[i] >= 0 and dp[i-1][j-v[i]]:
            dp[i][j] = True  # 이번에 더하는 경우
        if j+v[i] <= m and dp[i-1][j+v[i]]:
            dp[i][j] = True  # 이번에 빼는 경우
        if i == n and dp[i][j]:  # 마지막 연주곡
            ans = j
print(ans)
