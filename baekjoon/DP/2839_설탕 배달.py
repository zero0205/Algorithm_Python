n = int(input())
dp = [0, -1, -1, 1, -1, 1]

if n > 5:
    for i in range(6, n + 1):
        if dp[i-3] == -1:   # 3kg 안됨
            if dp[i-5] == -1:   # 만들 수 없는 경우
                dp.append(-1)
            else:               # 3kg X, 5kg O
                dp.append(dp[i-5] + 1)
        else:               # 3kg 됨
            if dp[i-5] == -1:   # 3kg O, 5kg X
                dp.append(dp[i-3] + 1)
            else:               # 3kg O, 5kg O
                dp.append(min(dp[i-3], dp[i-5]) + 1)
print(dp[n])