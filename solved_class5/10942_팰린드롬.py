import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

# 길이가 1
for i in range(n):
    dp[i][i] = 1
    
# 길이가 2
for i in range(1, n):
    if arr[i-1] == arr[i]:
        dp[i-1][i] = 1
        
# 길이가 3 이상
for i in range(2, n):
    for j in range(2, i+1):   # 문자열 길이 
        if arr[i] == arr[i-j] and dp[i-j+1][i-1] == 1:
            dp[i-j][i] = 1
        
        
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])