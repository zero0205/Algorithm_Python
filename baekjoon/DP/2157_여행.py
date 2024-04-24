import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
path = [[-1]*(n+1) for _ in range(n+1)]  # path[i][j] : i->j로 갈 때 기내식 점수
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:   # 동->서로 가는 경우에만 기내식 점수 저장
        path[a][b] = max(path[a][b], c)

# dp[i][j] : i번 도시까지 j개의 도시를 지나며 먹는 기내식 점수 총 합의 최대값
dp = [[-1]*(m+1) for _ in range(n+1)]
dp[1][1] = 0
for i in range(2, n+1):
    for j in range(2, m+1):
        for k in range(1, i):   # 나보다 동쪽에 있는 도시들 모두 탐색
            if dp[k][j-1] >= 0 and path[k][i] > 0:
                dp[i][j] = max(dp[i][j], dp[k][j-1]+path[k][i])
ans = 0
for i in range(1, m+1):
    ans = max(ans, dp[n][i])
print(ans)
