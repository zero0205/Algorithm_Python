import sys

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append([r, c])

# i번째부터 j번째까지 최소 연산 수 저장하는 배열
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 0
            continue
        for k in range(j-i):
            dp[i][j] = min(dp[i][j], dp[i][i+k] + dp[i+k+1][j] + matrix[i][0] * matrix[i+k][1] * matrix[j][1])
            
print(dp[0][n-1]) 