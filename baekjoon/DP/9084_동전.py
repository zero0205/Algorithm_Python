import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    dp = [0] * (m+1)
    for c in coin:
        if c > m:
            break
        dp[c] += 1
        for i in range(c+1, m+1):
            dp[i] += dp[i-c]
    print(dp[m])