# 다이나믹 프로그래밍
# 가장 긴 증가하는 부분 수열 알고리즘 이용
n = int(input())
sequence = list(map(int, input().split()))

up_dp = [1] * n  # 증가하는 수열의 길이를 저장할 리스트
down_dp = [1] * n  # 감소하는 수열의 길이를 저장할 리스트

# 증가하는 부분 수열
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)
# 감소하는 부분 수열
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if sequence[j] < sequence[i]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)

answer = 0       
for i in range(n):
    answer = max(answer, up_dp[i] + down_dp[i])
    
print(answer - 1)