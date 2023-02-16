import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
    exit()

stairs = []
for _ in range(n):
    stairs.append(int(input()))
    
dp = [[0, 0] for _ in range(n)]
dp[0][0] = stairs[0]            # 시작점 -> 1번째 칸
dp[1][0] = dp[0][0] + stairs[1] # 1번째 칸 -> 2번째 칸  (한 계단 오름)
dp[1][1] = stairs[1]            # 시작점 -> 2번째 칸 (두 계단 오름)
cnt = 0
for i in range(2, n):
    dp[i][0] = dp[i-1][1] + stairs[i]       # 한 계단 오름
    dp[i][1] = max(dp[i-2]) + stairs[i]     # 두 계단 오름

print(max(dp[n-1]))