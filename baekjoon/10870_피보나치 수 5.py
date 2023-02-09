dp = [0] * 21
dp[1] = 1
def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] == 0:
        dp[n] = fibonachi(n-1) + fibonachi(n-2)
    return dp[n]

print(fibonachi(int(input())))
