def factorial(n):
    if n <= 1:
        return 1
    dp = [1, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] * i)
    return dp[n]

n, m = map(int, input().split())
print(factorial(n) // factorial(m) // factorial(n-m))