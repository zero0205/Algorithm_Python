# https://www.acmicpc.net/problem/9095

dp = [0,1,2,4]

for i in range(4, 12):
    dp.append(dp[i-3] + dp[i - 2] + dp[i - 1])
    
# 테스트 케이스 개수 t 입력
t = int(input())
# 테스트케이스별 수행
for _ in range(t):
    n = int(input())
    print(dp[n])