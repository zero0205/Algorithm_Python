# n : 계단의 개수
n = int(input())
# 계단별 점수
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

# 한 계단 전 밟은 값과 두 계단 전 밟은 값을 모두 저장
dp = [[None] for _ in range(n + 1)]
dp[0] = (0, 0)
dp[1] = (stairs[1], stairs[1])
for i in range(2, n + 1):
    # 한 계단 전이면 두 칸 밟고 올라온 값만 사용 가능
    # 두 계단 전꺼면 한 칸 밟고 올라왔든 두 칸 밟고 올라왔든 상관X
    dp[i] = (dp[i - 1][1] + stairs[i], max(dp[i-2]) + stairs[i])  
    
print(max(dp[n]))