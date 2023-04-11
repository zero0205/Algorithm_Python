import sys
input = sys.stdin.readline

n = int(input())
consulting = [[0, 0]]
for _ in range(n):
    consulting.append(list(map(int, input().split())))
dp = [0] * (n+1) 
for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1]) # i일에 일하지 않더라도 i-1일까지 일한 이익보다는 크거나 같을 것
    end_date = i + consulting[i][0] - 1
    if end_date > n:    # 퇴사 이후에는 상담 X
        continue
    # 일이 끝나는 날의 dp 배열에 원래 저장된 값과 비교하여 최대 이익값 갱신
    dp[end_date] = max(dp[end_date], dp[i-1]+consulting[i][1])
print(max(dp))