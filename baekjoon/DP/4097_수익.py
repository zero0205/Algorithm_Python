from sys import stdin
input = stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    p = [int(input()) for _ in range(n)]
    ans = 0
    dp = [0]*n
    for i in range(n):
        dp[i] = max(dp[i-1]+p[i], p[i])  # 계속 이어나가기 vs 새로운 시작
    print(max(dp))
