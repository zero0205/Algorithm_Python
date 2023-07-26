##################### DP #####################
n = int(input())
cards = list(map(int, input().split()))
dp = [1 for _ in range(n)]  # cards[i]까지 봤을 때 최장증가부분수열의 길이 저장
for i in range(n):
    for j in range(i):
        if cards[i] > cards[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))