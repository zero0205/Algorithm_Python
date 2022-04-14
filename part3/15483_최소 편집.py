# https://www.acmicpc.net/problem/15483

str1 = input().strip()
str2 = input().strip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

# dp 테이블 초기화
for i in range(1, len(str1) + 1):
    dp[i][0] = i
for j in range(1, len(str2) + 1):
    dp[0][j] = j

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        # 두 문자가 같을 때
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 두 문자가 다름
        # => 삽입(왼쪽), 교체(대각선 왼쪽 위), 삭제(위쪽) 중 최소를 찾아 대입
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(dp[len(str1)][len(str2)])