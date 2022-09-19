step = list(map(int, input().split()))

def required_cost(now, next):
    if now == next:
        return 1
    if now == 0:
            return 2
    elif now % 2 == next % 2:
        return 4
    else:
        return 3
    
l = len(step)

# 왼발, 오른발, 인덱스
dp = [[[400001] * 5 for _ in range(5)] for _ in range(l)]

dp[0][0][0] = 0

for idx in range(1, l):
    nx = step[idx-1]
    for i in range(5):
        for j in range(5):
            # 왼발 이동
            dp[idx][nx][j] = min(dp[idx][nx][j], dp[idx-1][i][j] + required_cost(i, nx))
            # 오른발 이동
            dp[idx][i][nx] = min(dp[idx][i][nx], dp[idx-1][i][j] + required_cost(j, nx))
            
res = 400001
for i in range(5):
    for j in range(5):
        res = min(res, dp[l-1][i][j])
        
print(res)
            