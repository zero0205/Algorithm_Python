dp = [-1] * 31
dp[0], dp[1] = 1, 1
def factorial(n):
    if n <= 1:
        return 1
    if dp[n] == -1:
        dp[n] = n * factorial(n-1)
    return dp[n]

factorial(30)

for _ in range(int(input())):
    n, m = map(int, input().split())
    # mCn 조합 구하기
    print(dp[m] // (dp[n] * dp[m-n]))