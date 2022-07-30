n = int(input())

MOD = 1000000007

dp = dict()

def fib(n):
    if dp.get(n) != None:
        return dp[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        dp[n // 2 + 1] = fib(n // 2 + 1) % MOD
        dp[n // 2 - 1] = fib(n // 2 - 1) % MOD
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    if n % 2 == 1:
        dp[n // 2 + 1] = fib(n // 2 + 1) % MOD
        dp[n // 2] = fib(n // 2) % MOD
        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2
    
print(fib(n) % MOD)