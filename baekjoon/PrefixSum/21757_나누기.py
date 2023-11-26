import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 누적합
preSum = [0] * (n+1)
for i in range(1, n+1):
    preSum[i] = preSum[i-1] + arr[i-1]

ans = 0

if preSum[n] % 4 == 0:
    if preSum[n] == 0:  # 총합이 0인 경우
        zero_num = 0
        for i in range(1, n+1):
            if preSum[i] == 0:
                zero_num += 1
        # zero_num-1개 중 3개 뽑는 조합
        ans = ((zero_num-1)*(zero_num-2)*(zero_num-3)) // 6
    else:               # 총합이 0이상인 4의 배수
        partial_sum = preSum[n] // 4
        dp = [[0]*4 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, 4):
                dp[i][j] = dp[i-1][j]
                if preSum[i] == partial_sum * j:    # 이번에 자르기 가능한 경우
                    dp[i][j] += dp[i-1][j-1]
        ans = dp[n-1][3]
print(ans)
