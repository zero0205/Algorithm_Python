for _ in range(int(input())):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())

    dp = [[0] * (m+1) for _ in range(n+1)]  # i번째 동전까지 사용해서 금액 j를 만드는 방법의 수
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j >= coins[i]:
                dp[i][j] += dp[i][j-coins[i]]
    print(dp[n][m])
