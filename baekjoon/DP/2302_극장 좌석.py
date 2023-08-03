n = int(input())
fixed = []
for _ in range(int(input())):
    fixed.append(int(input())) 

dp = [1] * 41       # 좌석이 n개일 때 가능한 좌석 배치의 수(VIP 고려 X)
dp[2] = 2
dp[3] = 3

for i in range(4, 41):
    dp[i] = dp[i-2] + dp[i-1]

prev = 0
ans = 1
if fixed:
    for f in fixed: # VIP
        ans *= dp[f-prev-1]
        prev = f
    ans *= dp[n-prev]  # 마지막 부분 좌석 처리
else:
    ans = dp[n]
print(ans)