import sys
input = sys.stdin.readline

n, k = map(int, input().split())
info = [[]]
for _ in range(k):
    l, t = map(int, input().split())
    info.append([l, t])

dp = [[0] * (n+1) for _ in range(k+1)]    # 최대 중요도
for i in range(1, k+1):
    for j in range(n+1):
        if j < info[i][1]:  # 시간이 현재 과목에 필요한 공부시간보다 작은 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-info[i][1]]+info[i][0], dp[i-1][j])

print(dp[k][n])
