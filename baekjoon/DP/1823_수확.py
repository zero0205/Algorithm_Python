import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
v = [0]+[int(input()) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]


def recursion(l, r, cnt):
    if l > r:
        return 0
    if dp[l][r] != 0:
        return dp[l][r]
    dp[l][r] = max(v[l]*cnt+recursion(l+1, r, cnt+1),
                   v[r]*cnt+recursion(l, r-1, cnt+1))
    return dp[l][r]


print(recursion(1, n, 1))
