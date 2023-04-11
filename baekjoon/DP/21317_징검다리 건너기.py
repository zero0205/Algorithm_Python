n = int(input())
energy = [[0, 0]]   # i번째 돌에서 작은 점프 / 큰 점프 시 필요한 에너지
for _ in range(n-1):
    energy.append(list(map(int, input().split())))
k = int(input())
if n == 1:
    print(0)
    exit()
if n == 2:
    print(energy[1][0])
    exit()
dp = [[0, 0] for _ in range(n+1)]   # 큰 점프 안함 / 함
dp[2][0] = energy[1][0]
for i in range(3, n+1):
    # 큰 점프 아직 안 함
    dp[i][0] = min(dp[i-1][0]+energy[i-1][0], dp[i-2][0]+energy[i-2][1])
    if i == 4:
        dp[i][1] = k
    elif i == 5:
        dp[i][1] = min(dp[i-1][1]+energy[i-1][0], dp[i-3][0]+k)
    elif i > 5:
        dp[i][1] = min(dp[i-1][1]+energy[i-1][0], dp[i-2][1]+energy[i-2][1], dp[i-3][0]+k)
if n == 3:
    print(dp[n][0])
else:
    print(min(dp[n]))