from itertools import combinations

n, m = map(int, input().split())
wok = list(map(int, input().split()))
possible = set(wok)
for comb in combinations(wok, 2):
    possible.add(sum(comb))

dp = [10001] * (n+1)    # n그릇의 짜장면을 만들기 위해 필요한 최소 요리 횟수
dp[0] = 0
for i in range(1, n+1):
    for j in possible:
        if (i-j) >= 0 and dp[i-j]+1 < dp[i]:
            dp[i] = dp[i-j]+1
print(dp[n] if dp[n] != 10001 else -1)
